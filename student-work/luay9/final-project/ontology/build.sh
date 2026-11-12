#!/usr/bin/env bash
# Rebuild the Meeting & Mandate ontology and every file in results/ from scratch.
# Run from this folder:  bash build.sh /path/to/CommonCoreOntologiesMerged.ttl
# Tested with ROBOT 1.9.10, Java 25, CCO v2.2 (2026-08-13). See BUILD.md.
set -euo pipefail

CCO="${1:?usage: bash build.sh /path/to/CommonCoreOntologiesMerged.ttl}"
R="java -jar ${ROBOT_JAR:-$HOME/tools/robot.jar}"
ONTO="--input cco-module.ttl --input meeting-mandate.ttl --input test-individuals.ttl"
mkdir -p results

echo "1. Extract the BFO + CCO module"
$R extract --input "$CCO" --method BOT --term-file cco-terms.txt \
  --individuals exclude --output cco-module.ttl

echo "2. Merge and reason with HermiT"
$R merge $ONTO \
  reason --reasoner hermit --axiom-generators "SubClass ClassAssertion" --include-indirect true \
  --output meeting-mandate-full.ttl

echo "3. Check the reasoner's results"
$R query --input meeting-mandate-full.ttl \
  --query queries/checks/decision-meetings.rq results/step7-decision-meetings.csv \
  --query queries/checks/mandate-types.rq     results/step7-mandate-types.csv \
  --query queries/checks/class-hierarchy.rq   results/step7-class-hierarchy.csv \
  --query queries/checks/cq4-control.rq       results/cq4-control-reasoned.csv
$R merge $ONTO query --query queries/checks/cq4-control.rq results/cq4-control-asserted.csv

echo "4. Failure tests"
# 4a. A mandate that is also a person must make the ontology inconsistent.
if $R merge $ONTO --input tests/bad-mandate-person.ttl reason --reasoner hermit \
     > results/step8-inconsistency.txt 2>&1; then
  echo "FAIL: bad-mandate-person.ttl was not reported inconsistent" >&2; exit 1
fi
grep -v "^WARNING:" results/step8-inconsistency.txt > results/step8.tmp || true
mv results/step8.tmp results/step8-inconsistency.txt
$R merge $ONTO --input tests/bad-mandate-person.ttl \
  explain --reasoner hermit --mode inconsistency --explanation results/step8-explanation.md
# 4b. A directive by someone with no authority role must not make a decision meeting.
$R merge $ONTO --input tests/no-authority-probe.ttl \
  reason --reasoner hermit --axiom-generators "ClassAssertion" --include-indirect true \
  query --query queries/checks/decision-meetings.rq results/probe-no-authority.csv

echo "5. Answer the competency questions"
$R query --input meeting-mandate-full.ttl \
  --query queries/cq1.rq results/cq1.csv \
  --query queries/cq2.rq results/cq2.csv \
  --query queries/cq3.rq results/cq3.csv \
  --query queries/cq4.rq results/cq4.csv \
  --query queries/cq5.rq results/cq5.csv

echo "6. Quality report (this ontology only, not CCO)"
$R report --input meeting-mandate.ttl --profile report-profile.txt \
  --fail-on none --output results/report.tsv

echo "7. Sustained extendability: ingest the documents one at a time"
# Each document in documents/ is merged onto the documents accepted before it,
# reasoned with HermiT and queried with CQ1-CQ5. A document that makes the base
# inconsistent is rejected; an earlier answer that stops holding fails the build.
python ingest.py

echo "Done. Results are in results/."
