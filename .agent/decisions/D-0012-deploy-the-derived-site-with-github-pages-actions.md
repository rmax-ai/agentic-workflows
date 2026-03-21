# D-0012 — Deploy the derived site with GitHub Pages actions

- Status: accepted
- Decision: Deploy the generated MkDocs site through a GitHub Actions workflow that runs the repository validation and site-generation pipeline on `main`, uploads `build/site` as a Pages artifact, and publishes through GitHub Pages.
- Rationale: This keeps deployment automation derived from the same canonical build path used locally, avoids committing generated HTML, and makes publication reproducible without adding a second hosting-specific authoring flow.
