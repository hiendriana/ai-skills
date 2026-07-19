---
name: knowledge-curator
description: Review and non-destructively process Markdown notes from a personal knowledge repository inbox into durable domain knowledge. Use when Codex is asked to assess, curate, integrate, or process one inbox note or multiple pending notes while preserving source notes, preferring existing pages, avoiding duplication, preserving evidence and links, and reporting proposals before applying changes.
---

# Knowledge Curator

Integrate durable, verified knowledge from inbox captures without treating the
captures as authoritative or consuming them.

## Safety rules

- Never delete, archive, move, clear, prune, or reorganize inbox notes.
- Never run `rm`, `git clean`, or equivalent destructive cleanup commands.
- Never overwrite or substantially rewrite a captured note's body.
- Preserve source metadata, attribution, quotations, links, uncertainty, and
  personal observations as provenance.
- Modify a source note only to add or update small lifecycle front matter.
- Keep every processed or rejected note recoverable in the inbox.
- Leave retention and cleanup decisions to a separate `knowledge-janitor`
  skill.

Read [the inbox lifecycle guide](guides/inbox-lifecycle.md) before changing note
metadata. Read [the evidence and conflicts guide](guides/evidence-and-conflicts.md)
when deciding whether claims are safe to integrate.

## Workflow

Follow this sequence:

```text
Capture -> Proposal -> Review -> Apply -> Mark processed
```

### 1. Establish scope

1. Locate the knowledge repository root and read its `AGENTS.md`, root
   `README.md`, and `inbox/README.md` when present.
2. Interpret a named Markdown path as single-note mode. Interpret a request to
   process the inbox as multiple-note mode.
3. In multiple-note mode, enumerate Markdown notes under `inbox/`, excluding
   policy files such as `README.md` and `AGENTS.md`.
4. Treat missing lifecycle front matter as `pending`.
5. Ignore `processed` notes unless the user explicitly requests reprocessing.
   Ignore `rejected` notes unless the user explicitly requests reconsideration.
6. Include `pending` and `needs-review` notes, while preserving their different
   states in the report.
7. Inspect Git status and preserve unrelated changes.

### 2. Select the mode

Use proposal mode by default. Enter apply mode only when the invocation
explicitly asks to apply changes or approves a previously reported proposal.

In proposal mode:

- inspect notes, evidence, existing knowledge, and candidate destinations;
- propose integrations and lifecycle outcomes;
- do not modify domain pages or note metadata;
- stop after the review report.

In apply mode:

- apply only the explicitly requested or approved integrations;
- update relevant indexes and cross-links;
- update lifecycle metadata only after validating the integration;
- leave every source note in place;
- produce the processing report.

### 3. Review knowledge and evidence

Treat every note as captured input and every claim as a proposal. Distinguish
sourced facts, attributable experience, interpretation, recommendations,
questions, and speculation. Preserve uncertainty and flag contradictions with
existing knowledge.

Do not invent missing context or promote unsupported claims. Verify important
claims with authoritative evidence when required by repository policy. If safe
integration is not possible, propose or apply `needs-review`; use `rejected`
only with explicit user approval or an invocation that explicitly permits
rejection.

### 4. Locate the durable owner

Inventory relevant domain indexes and pages before proposing a destination.

- Choose the narrowest durable owner.
- Prefer updating an existing page over creating a new page.
- Create a page only when the material is substantial, independently useful,
  clearly scoped, and has no suitable existing owner.
- Search for semantic overlap, not only matching filenames.
- Link to a primary owner instead of duplicating explanations.
- Keep repository-specific implementation and operations in their source
  repository; summarize and link from the knowledge base.
- Preserve useful links, attribution, provenance, and uncertainty.

For a previously processed note that the user explicitly asks to reprocess,
verify every recorded `integrated_into` destination before proposing changes.
Do not re-add claims already represented there.

### 5. Report before applying

In proposal mode, report for every note:

1. note path and current status;
2. durability assessment and rationale;
3. verified claims or attributable observations worth retaining;
4. claims to omit and why;
5. proposed pages to create or update;
6. links and provenance to preserve;
7. proposed lifecycle status;
8. uncertainties, conflicts, and decisions requiring user input.

For multiple notes, add a consolidated plan and identify overlap between notes
or shared destinations. Do not apply the proposal in the same turn unless the
invocation explicitly selected apply mode.

### 6. Apply idempotently

1. Recheck Git status, note status, and destination contents.
2. Apply only approved durable claims that are not already represented.
3. Synthesize in the destination owner's style; do not paste the note body.
4. Update indexes and cross-links only when needed.
5. Validate the knowledge changes before updating note lifecycle metadata.
6. Mark a successfully integrated note `processed`, recording the integration
   date and destination paths.
7. Mark a note `needs-review` when safe integration remains blocked. Mark it
   `rejected` only under the explicit rejection rule.
8. Change only lifecycle fields in front matter. Preserve the captured body and
   all source metadata exactly.

If any knowledge edit or validation fails, do not mark the note `processed`.
Do not claim a processing commit unless the relevant changes are actually
contained in that commit.

## Validate and report

Verify modified relative links and referenced paths, inspect the final diff,
and check for duplicated knowledge, unsupported claims, lost uncertainty,
secrets, private content, and unrelated changes. Confirm that every source note
still exists and its captured body and provenance remain unchanged.

For every note handled in apply mode, report:

1. note path;
2. previous and new status;
3. destination pages created;
4. destination pages updated;
5. claims integrated;
6. claims omitted;
7. uncertainties or conflicts;
8. links added;
9. whether manual review remains required.

Also report validation performed and any uncommitted changes. Do not claim that
a check passed unless it was run.
