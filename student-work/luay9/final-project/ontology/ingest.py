"""Sustained-extendability test: ingest the synthetic documents one at a time.

For each document in documents/manifest.tsv, in order:

  1. Merge the base (CCO module + meeting-mandate.ttl), every document accepted
     so far, and the new one. Reason with HermiT (via ROBOT).
     If the merge is inconsistent, the document is REJECTED and the base stays
     as it was.
  2. Answer CQ1-CQ5 on the reasoned snapshot.
  3. Regression: every answer from the previous accepted snapshot must still
     hold. A row with an empty cell (an OPTIONAL not yet bound) is "still true"
     if a new row agrees on every filled cell: unknown becoming known is depth,
     not breakage.
  4. Measure what the document added (depth, breadth, language).

Then it writes one named graph per accepted document (program-a.trig), runs the
X01/X02/X04/V04 queries on it, checks that the incremental build ends with the
same CQ answers as the one-shot v0.1 build (results/cq*.csv), and writes
results/extendability/ingest-log.md and ingest-log.csv.

Run from this folder:  python ingest.py
Needs ROBOT (ROBOT_JAR, default ~/tools/robot.jar), Java and rdflib.
Exits non-zero if any expectation in the manifest is not met.
"""

import csv
import os
import shutil
import subprocess
import sys
from pathlib import Path

from rdflib import Dataset, Graph, Literal, Namespace, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SKOS

HERE = Path(__file__).resolve().parent
OUT = HERE / "results" / "extendability"
ROBOT_JAR = os.environ.get("ROBOT_JAR", str(Path.home() / "tools" / "robot.jar"))
BASE_FILES = ["cco-module.ttl", "meeting-mandate.ttl"]
CQS = ["cq1", "cq2", "cq3", "cq4", "cq5"]
X_QUERIES = ["x01-provenance", "x02-what-changed", "x04-corroboration", "v04-new-terms"]
GRAPH_NS = "https://github.com/luay9/meeting-mandate/graph/"
MM = Namespace("https://github.com/luay9/meeting-mandate#")
DCT = Namespace("http://purl.org/dc/terms/")
LABEL_PROPS = {SKOS.prefLabel, SKOS.altLabel, SKOS.scopeNote}
DECLARATION_TYPES = {OWL.ObjectProperty, OWL.AnnotationProperty}


def robot(args):
    cmd = ["java", "-jar", ROBOT_JAR] + args
    return subprocess.run(cmd, cwd=HERE, capture_output=True, text=True)


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if not rows:            # ROBOT writes an empty file, with no header, for zero rows
        return [], []
    return rows[0], [tuple(r) for r in rows[1:]]


def still_holds(old_row, new_rows):
    """An old answer holds if some new row agrees on every non-empty cell."""
    return any(all(o == "" or o == n for o, n in zip(old_row, new)) for new in new_rows)


def content_triples(path, graph_iri):
    """The document's own assertions: no relation declarations, no header."""
    g = Graph().parse(HERE / path)
    declared = {s for s, o in g.subject_objects(RDF.type) if o in DECLARATION_TYPES}
    return {(s, p, o) for s, p, o in g if s != graph_iri and s not in declared}, g


def individuals(triples):
    return {s for s, p, o in triples if p == RDF.type and o == OWL.NamedIndividual}


def types_used(triples):
    return {o for s, p, o in triples if p == RDF.type and o != OWL.NamedIndividual}


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    with open(HERE / "documents" / "manifest.tsv", newline="", encoding="utf-8") as f:
        manifest = list(csv.DictReader(f, delimiter="\t"))

    base_graph = Graph()
    for f in BASE_FILES:
        base_graph.parse(HERE / f)
    base_labels = {(s, o) for s, p, o in base_graph if p in (SKOS.prefLabel, SKOS.altLabel)}

    accepted, log, failures = [], [], []
    prev_answers = None
    seen_subjects, seen_individuals, seen_types = set(), set(), set()
    seen_labels = set(base_labels)

    for doc in manifest:
        doc_id, path = doc["id"], "documents/" + doc["file"]
        graph_iri = URIRef(GRAPH_NS + doc_id)
        snap_dir = OUT / f"after-{doc_id}"
        snap_dir.mkdir()
        snapshot = snap_dir / "snapshot-reasoned.ttl"

        inputs = []
        for f in BASE_FILES + [d["path"] for d in accepted] + [path]:
            inputs += ["--input", f]
        query_args = []
        for cq in CQS:
            query_args += ["--query", f"queries/{cq}.rq", str(snap_dir / f"{cq}.csv")]
        result = robot(["merge"] + inputs
                       + ["reason", "--reasoner", "hermit", "--axiom-generators",
                          "SubClass ClassAssertion", "--include-indirect", "true",
                          "--output", str(snapshot)]
                       + ["query"] + query_args)

        triples, _ = content_triples(path, graph_iri)
        row = {"id": doc_id, "type": doc["type"], "date": doc["date"],
               "expected": doc["expected"], "triples": len(triples)}

        if result.returncode != 0:
            row["status"] = "rejected"
            reason = "inconsistent" if "inconsistent" in (result.stdout + result.stderr).lower() \
                else "ROBOT error"
            row["note"] = f"{reason}; base kept as after {accepted[-1]['id'] if accepted else 'nothing'}"
            (snap_dir / "robot-output.txt").write_text(
                "\n".join(l for l in (result.stdout + result.stderr).splitlines()
                          if not l.startswith("WARNING")), encoding="utf-8")
            robot(["merge"] + inputs + ["explain", "--reasoner", "hermit", "--mode", "inconsistency",
                   "--explanation", str(snap_dir / "explanation.md")])
            if doc["expected"] != "rejected":
                failures.append(f"{doc_id} was rejected but was expected to be accepted:\n{result.stderr[-2000:]}")
            log.append(row)
            continue
        if doc["expected"] == "rejected":
            failures.append(f"{doc_id} was expected to be rejected, but the reasoner accepted it")

        # Regression and coverage
        answers = {cq: read_csv(snap_dir / f"{cq}.csv") for cq in CQS}
        broken = []
        if prev_answers:
            for cq in CQS:
                for old in prev_answers[cq][1]:
                    if not still_holds(old, answers[cq][1]):
                        broken.append(f"{cq}: {old}")
        row["cqs_answered"] = sum(1 for cq in CQS if answers[cq][1])
        row["answer_rows"] = sum(len(answers[cq][1]) for cq in CQS)
        row["newly_answerable"] = ", ".join(
            cq.upper() for cq in CQS
            if answers[cq][1] and (not prev_answers or not prev_answers[cq][1]))
        row["regressions"] = len(broken)
        if broken:
            failures.append(f"{doc_id} broke earlier answers: {broken}")
        prev_answers = answers

        # What the document added
        new_inds = individuals(triples) - seen_individuals
        on_existing = {t for t in triples if t[0] in seen_subjects and t[1] not in LABEL_PROPS}
        links_in = {t for t in triples if t[0] not in seen_subjects and t[2] in seen_individuals}
        used = types_used(triples) - {SKOS.Concept}
        first_types = used - seen_types
        new_classes = {s for s, p, o in triples if p == RDF.type and o == OWL.Class}
        labels = {(s, o) for s, p, o in triples if p in (SKOS.prefLabel, SKOS.altLabel)}
        new_labels = labels - seen_labels
        parked = {s for s, p, o in triples if p == RDF.type and o == SKOS.Concept}

        def short(u):
            lab = base_graph.value(u, RDFS.label)
            return str(lab) if lab else u.split("#")[-1].split("/")[-1]

        row.update({
            "status": "accepted",
            "new_individuals": len(new_inds),
            "facts_on_existing": len(on_existing),
            "links_into_base": len(links_in),
            "classes_first_used": "; ".join(sorted(short(c) for c in first_types)),
            "classes_reused": f"{len(used & seen_types)}/{len(used)}",
            "new_owl_classes": len(new_classes),
            "new_labels": len(new_labels),
            "labels_added": "; ".join(sorted(f"{l} ({l.language})" for _, l in new_labels)),
            "parked_terms": "; ".join(sorted(short(c) for c in parked)),
            "note": "",
        })
        if new_classes:
            failures.append(f"{doc_id} minted OWL classes {new_classes}: a new class needs a CQ and goes in meeting-mandate.ttl")
        log.append(row)

        accepted.append({"id": doc_id, "path": path, "iri": graph_iri})
        seen_subjects |= {s for s, p, o in triples}
        seen_individuals |= individuals(triples)
        seen_types |= types_used(triples)
        seen_labels |= labels

    # One named graph per accepted document
    ds = Dataset()
    base = ds.graph(URIRef(GRAPH_NS + "base"))
    for t in base_graph:
        base.add(t)
    for d in accepted:
        g = ds.graph(d["iri"])
        g.parse(HERE / d["path"])
    ds.namespace_manager.bind("mm", MM)
    trig = OUT / "program-a.trig"
    ds.serialize(destination=str(trig), format="trig")

    for q in X_QUERIES:
        text = (HERE / "queries" / "extendability" / f"{q}.rq").read_text(encoding="utf-8")
        res = ds.query(text)
        with open(OUT / f"{q}.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow([str(v) for v in res.vars])
            for r in res:
                w.writerow(["" if v is None else str(v) for v in r])

    # Incremental build vs. one-shot v0.1 build
    last = OUT / f"after-{accepted[-1]['id']}"
    same = []
    for cq in CQS:
        h1, r1 = read_csv(last / f"{cq}.csv")
        h0, r0 = read_csv(HERE / "results" / f"{cq}.csv")
        ok = h1 == h0 and sorted(r1) == sorted(r0)
        same.append((cq, ok))
        if not ok:
            failures.append(f"{cq}: incremental answers differ from the one-shot v0.1 build")

    # Keep the repo light: drop the reasoned snapshots, keep the answers
    for d in OUT.glob("after-*/snapshot-reasoned.ttl"):
        d.unlink()

    write_log(log, same, failures)
    if failures:
        print("FAILED:\n" + "\n".join(failures), file=sys.stderr)
        sys.exit(1)
    print(f"OK: {len(accepted)} documents accepted, "
          f"{sum(1 for r in log if r['status'] == 'rejected')} rejected, 0 regressions. "
          f"See {OUT.relative_to(HERE)}/ingest-log.md")


def write_log(log, same, failures):
    fields = ["id", "type", "date", "expected", "status", "triples", "new_individuals",
              "facts_on_existing", "links_into_base", "classes_reused", "classes_first_used", "new_owl_classes",
              "new_labels", "labels_added", "parked_terms", "cqs_answered", "answer_rows",
              "newly_answerable", "regressions", "note"]
    with open(OUT / "ingest-log.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in log:
            w.writerow(r)

    L = ["# Ingest log: Program A, one document at a time", "",
         "Generated by `ingest.py`. Do not edit by hand.", "",
         "| Doc | Type | Expected | Status | Triples | New individuals | Facts on existing nodes "
         "| Links into base | Classes reused | Classes first used | New OWL classes | New labels | CQs answered "
         "| Newly answerable | Regressions |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in log:
        if r["status"] == "rejected":
            L.append(f"| {r['id']} | {r['type']} | {r['expected']} | **rejected** | {r['triples']} "
                     f"| | | | | | | | | | {r['note']} |")
            continue
        L.append(f"| {r['id']} | {r['type']} | {r['expected']} | accepted | {r['triples']} "
                 f"| {r['new_individuals']} | {r['facts_on_existing']} | {r['links_into_base']} | {r['classes_reused']} "
                 f"| {r['classes_first_used'] or '—'} | {r['new_owl_classes']} | {r['new_labels']} "
                 f"| {r['cqs_answered']}/5 | {r['newly_answerable'] or '—'} | {r['regressions']} |")
    L += ["", "## Words each document added", ""]
    for r in log:
        if r["status"] == "accepted" and (r["labels_added"] or r["parked_terms"]):
            parked = f" · parked as SKOS concept: {r['parked_terms']}" if r["parked_terms"] else ""
            L.append(f"- **{r['id']}**: {r['labels_added'] or 'none'}{parked}")
    L += ["", "## Incremental build vs. the one-shot v0.1 build", "",
          "| CQ | Same answers as `results/` |", "|---|---|"]
    L += [f"| {cq.upper()} | {'yes' if ok else '**no**'} |" for cq, ok in same]
    L += ["", "## Result", "", "PASS" if not failures else "FAIL:\n\n" + "\n".join(f"- {x}" for x in failures), ""]
    (OUT / "ingest-log.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
