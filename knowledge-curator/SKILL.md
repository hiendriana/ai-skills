---
name: knowledge-curator
description: Review and integrate unverified Markdown captures and manifested PDF or image capture bundles from a personal knowledge repository inbox into durable domain knowledge, then move successfully validated captures into a policy-defined processed recycle bin. Use when Codex is asked to assess, curate, register, integrate, or process active inbox notes, PDFs, JPEGs, PNGs, or WebP images while preserving proposal-before-apply review, evidence, provenance, idempotency, and recoverability boundaries.
---

# Knowledge Curator

Integrate durable, verified knowledge from inbox captures without treating the
captures as authoritative.

## Safety rules

- Require repository policy that explicitly defines the active inbox and its
  `processed/` recycle-bin workflow before moving a capture.
- Never delete captures or run destructive cleanup commands.
- Never overwrite or substantially rewrite a capture's body or provenance.
- Never modify, execute, or externally upload a bundled source file.
- Keep `pending` and `needs-review` captures in the active inbox.
- Move a capture only after its approved integration validates successfully.
- Never commit unless the user explicitly requests a commit.

Read [the inbox lifecycle guide](guides/inbox-lifecycle.md) before changing note
metadata or paths. Read [the evidence and conflicts guide](guides/evidence-and-conflicts.md)
when deciding whether claims are safe to integrate. Read [the capture bundle
guide](guides/capture-bundles.md) before registering or processing a PDF or
image.

## Workflow

Follow this sequence:

```text
Capture -> Curate -> Validate -> Move to processed/ -> Commit -> Janitor review -> Approved removal
```

### 1. Establish scope

1. Locate the repository root and read its `AGENTS.md`, root `README.md`, and
   inbox policy files when present.
2. Confirm that repository policy explicitly documents the `processed/`
   recycle-bin lifecycle. Without it, propose knowledge integration but do not
   move captures or invent lifecycle conventions.
3. Interpret a named Markdown capture or manifested bundle as single-capture
   mode. Interpret a request to process the inbox as multiple-capture mode.
4. In multiple-capture mode, enumerate standalone Markdown captures, bundle
   manifests named `capture.md`, and loose supported PDF or image files under
   active inboxes. Exclude policy files such as `README.md` and `AGENTS.md`,
   attachments declared by a bundle manifest, and every `processed/` directory
   and its entire subtree.
5. Treat missing lifecycle front matter as `pending`. Include `pending` and
   `needs-review` captures while preserving their distinct states.
6. Skip `processed` captures by default. If explicitly asked to revisit one,
   verify its destinations and do not reintegrate represented claims.
7. Inspect Git status and preserve unrelated changes.
8. Keep repository maintenance outside the curation scope. Remove temporary or
   generated execution artifacts created by the workflow from the working tree
   before completing the task, and never commit them; Python `__pycache__/`
   directories and `*.pyc` files are examples, not an exhaustive list. Do not
   modify `.gitignore` or other repository-wide configuration solely to
   accommodate such artifacts unless that change is explicitly in scope.
   Instead, report a missing ignore rule that is likely to cause recurring
   pollution as a recommended repository-maintenance change.

### 2. Select the mode

Use proposal mode by default. Enter apply mode only when the invocation
explicitly requests changes or approves a previously reported proposal.

In proposal mode, inspect captures, evidence, existing knowledge, and candidate
destinations; report proposed integrations and lifecycle outcomes; change
nothing. Treat a loose supported PDF or image as an unregistered capture and
propose its bundle path and manifest; do not register or move it yet.

In apply mode, apply only approved integrations, validate them, update lifecycle
metadata, and move each successfully processed capture to its policy-defined
`processed/` directory. Do not move a capture if integration or validation
fails. Register a loose file only when the approved proposal names that file and
its bundle path.

### 3. Curate unverified input

Treat every capture as input and every claim as a proposal. Distinguish sourced
facts, attributable experience, interpretation, recommendations, questions,
and speculation. Preserve uncertainty and flag contradictions.

Do not invent missing context or promote unsupported claims. Verify important
claims when repository policy requires it. If safe integration is blocked, use
`needs-review`; use `rejected` only with explicit authority and leave that
capture in the active inbox.

### 4. Locate the durable owner

Inventory relevant pages and indexes before selecting a destination.

- Choose the narrowest durable owner and prefer an existing page.
- Create a page only when independently useful material has no suitable owner.
- Search for semantic overlap and link to a primary owner instead of duplicating
  explanations.
- Keep source-repository implementation and operations in that repository;
  summarize and link from the knowledge base.
- Preserve useful evidence, attribution, provenance, and uncertainty.

### 5. Report before applying

For every capture, report its path and status, durability assessment, claims to
integrate and omit, proposed destinations, provenance to preserve, proposed
lifecycle outcome, and unresolved decisions. In multiple-capture mode, add a
consolidated plan and identify overlap. Do not apply the proposal in the same
turn unless apply mode was explicitly selected.

### 6. Apply idempotently

1. Recheck Git status, capture status and path, approved scope, and destination
   contents.
2. Stop if the capture is already processed and represented at every recorded
   destination; do not duplicate integration or lifecycle moves.
3. Apply only approved durable claims not already represented. Synthesize in
   the destination owner's style rather than copying the capture body.
4. Update indexes and cross-links only when needed.
5. Validate the integration before changing capture metadata or location.
6. After successful validation, set `status: processed`, record `processed_at`,
   and record repository-relative `integrated_into` paths.
7. Move the complete standalone capture or bundle directory, with body,
   provenance, manifest, and source files intact, from the active inbox to that
   inbox's policy-defined `processed/` directory. Resolve destination-name
   collisions through the inbox lifecycle guide; never overwrite, replace, or
   repurpose an unrelated processed capture.
8. Update links affected by the move. Avoid durable-page backlinks to the
   disposable processed capture unless the link remains genuinely useful.

If any integration, validation, metadata update, or move fails, leave the
capture unprocessed in the active inbox or restore the operation to that state.
Do not claim Git recoverability based only on the file's presence under
`processed/`.

## Validate and report

Verify modified links and paths, destination coverage, idempotency, the complete
capture body and provenance, the final diff, sensitive content, unsupported
claims, and unrelated changes. Determine tracking and commit evidence
separately; a tracked working-tree path is not necessarily present in a commit.
For a bundle, also verify declared membership, media types, byte sizes, SHA-256
values, extraction coverage, and that every member moved together.

For every capture applied, report:

1. original path and processed path;
2. previous and new status;
3. destination pages;
4. claims integrated and omitted;
5. validation performed;
6. whether the processed capture is currently Git-tracked;
7. whether an existing commit contains the processed capture, with evidence;
8. whether manual review remains required.

For a bundle, also report every source file, its detected media type and hash,
the extraction or OCR method and limitations, tool availability and versions,
and tracking and commit evidence for every member.

Also report uncommitted changes. Do not claim a check passed unless it ran, and
do not commit unless explicitly requested.
