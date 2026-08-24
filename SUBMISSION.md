# Submission Guide

This course is remote and asynchronous. GitHub is the primary environment for submitting and discussing course work.

## Submission Summary

| Work | Submission Method |
|---|---|
| Undergraduate Discussion Questions | GitHub Discussions |
| Undergraduate Final Project Draft | GitHub pull request |
| Undergraduate Final Project | GitHub pull request |
| Graduate Presentation 1 | Link posted in GitHub Discussions |
| Graduate Presentation 2 | Link posted in GitHub Discussions |
| Graduate Final Project | GitHub pull request |
| General questions and project help | GitHub Discussions |

## Undergraduate Discussion Questions

1. Open the course [Discussions](https://github.com/Applied-Ontology-Education/Ontology-and-Intel-Analysis/discussions).
2. Find the Discussion with the title shown in the relevant assignment file.
3. Post your response in that Discussion.
4. Keep the response to **500 words or fewer** unless the prompt states otherwise.
5. Use citations where appropriate.
6. Submit during the weekly module identified in the course schedule.

Do not open a pull request for a Discussion Question.

## Graduate Presentations

Graduate students submit a link to each recorded presentation through the designated GitHub Discussion.

Your post should include:

```markdown
## Presentation
Presentation 1 or Presentation 2

## Title
Your presentation title

## Design Pattern
One or two sentences identifying the intelligence-analysis problem modeled.

## Recording
Link to recording

## Supporting Material
Link to slides, diagram, ontology artifact, or other supporting material if applicable.
```

Do not place a recording in the repository unless specifically instructed to do so.

## Project Draft and Final Project

Ontology projects are submitted through GitHub pull requests.

### 1. Fork the Repository

If you have not already done so, fork the course repository into your GitHub account.

### 2. Create a Project Branch

Examples:

```bash
git switch -c project-draft
```

or:

```bash
git switch -c final-project
```

### 3. Add Your Work

Create a directory for your work using a clear identifier, for example:

```text
student-work/
└── your-github-username/
    ├── project-draft/
    └── final-project/
```

If the repository does not yet contain `student-work/`, you may create it in your branch.

Do not modify another student's directory.

### 4. Include the Required Artifacts

Follow the relevant assignment instructions.

### 5. Commit and Push

```bash
git add .
git commit -m "Submit final ontology project"
git push -u origin final-project
```

### 6. Open a Pull Request

Open a pull request from your branch into the course repository.

Use a title such as:

```text
Final Project — your-github-username — Project Title
```

Your pull request description should contain:

```markdown
## Assignment
Final Project

## Project
Project title

## Summary
Briefly describe the intelligence-analysis problem and the ontology you developed.

## Files
List the principal files being submitted.

## Validation
Explain how you checked the ontology, including any reasoning, competency-question testing, or other validation performed.

## Known Limitations
List important limitations or unresolved modeling questions.
```

## Sensitive Information

This is a public educational repository.

Do **not** upload:

- classified information;
- controlled unclassified information;
- export-controlled material;
- proprietary or employer-restricted information;
- operational intelligence;
- personal data;
- credentials or passwords;
- API keys or tokens; or
- any other material you are not authorized to publish.

Use only public, synthetic, fictional, or otherwise authorized material in course work.

## Getting Help

Use GitHub Discussions for submission questions and technical problems.
