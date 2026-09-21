---
name: book-curator
description: Identify, deduplicate, import, research, create, and safely enrich book records in knowledge bases that define their own book configuration. Use for individual book captures, reading-list imports, reader-reception research, or book-record refreshes; do not use it to invent a knowledge base's schema, taxonomy, paths, or personal judgments.
---

# Book Curator

Turn titles, identifiers, URLs, recommendations, inbox mentions, and normalized
imports into one well-sourced record per logical book while preserving the
reader's decisions and the target knowledge base's ownership.

## Establish the contract

Before creating or updating a record:

1. Read applicable `AGENTS.md`, README and policy files, then locate the
   repository's book schema, configuration, template, examples, and import
   policy. Follow an explicit configuration path supplied by the repository or
   user first. Otherwise inspect conventional repository-local candidates such
   as `book-curator.yaml`, `.book-curator.yaml`, and
   `config/book-curator.yaml` (or `.yml`/`.json` variants), plus book-specific
   policy files referenced by the repository documentation.
2. Resolve the contract described in
   [references/configuration-contract.md](references/configuration-contract.md).
   Repository configuration is authoritative, including any explicit
   edition-per-record override.
3. Inspect existing book records and the template before assuming how a field
   is represented. Treat rendered views, dashboards, and application syntax as
   repository-owned presentation, not part of this skill.
4. Inspect Git status and preserve unrelated work. Do not commit, publish,
   delete, or move captures unless the user and repository policy authorize it.

If no usable configuration exists, stop before permanent KB mutation. Report
the missing decisions and offer the minimal bootstrap contract from the
configuration reference; do not silently create a folder hierarchy, taxonomy,
template, status vocabulary, dashboard, or import staging area.

## Choose the workflow

- **Single capture:** Read
  [references/capture-and-update.md](references/capture-and-update.md). Resolve
  the work, search for duplicates, then create or safely update one record.
- **Import:** Read [references/imports.md](references/imports.md). Normalize and
  deduplicate first; use lightweight, review-needed records by default.
- **Full enrichment or refresh:** Read
  [references/research.md](references/research.md). Select the fiction or
  nonfiction research profile and preserve source-specific reception.

When an active inbox capture is involved, also follow the knowledge base's
generic inbox lifecycle. This skill owns book-domain interpretation, not a
generic capture's movement or disposal.

## Domain invariants

- Default to one record per logical work. Keep edition and translation data
  inside it when useful. Split records only when authoritative KB configuration
  explicitly uses an edition-level model.
- Match exact stable identifiers first (ISBN-13 after normalization, Goodreads
  ID, provider source ID, or ASIN). Fall back to normalized title plus author,
  and treat uncertain collisions as review items rather than matches.
- Reading state, ownership, personal priority, personal rating, and language
  actually read are independent. Never infer one from another.
- Semantically distinguish a candidate, shortlist, currently reading, read,
  dropped-before-starting, and abandoned-after-starting. Map those concepts to
  configured values. Use one configured decision-reason concept for dropped or
  abandoned records.
- Never assign or overwrite personal priority, personal rating, reading
  language, review, notes, contexts, decision reason, or any other user-owned
  value. Default expectations of 1–5 priority and whole-value 1–5 personal
  ratings are bootstrap semantics only; configured scales control.
- Ownership may contain multiple configured formats such as physical, digital,
  or audiobook. Physical location and digital-library provider/URL/item ID are
  optional and configuration-driven. Do not require filesystem paths or infer
  borrowing/lending behavior.
- Preserve why and how the user saved the book separately from researched
  summary, reasons to read, and reasons to skip. Never replace original
  recommendation context with generated justification.
- Use configured controlled genres, flexible topics, and curated contexts. Do
  not proliferate controlled values; suggest or flag an unmatched value under
  repository policy.
- Represent unknowns as unknown/empty according to the schema. Do not guess an
  ambiguous work, edition, identifier, rating, or source association.

## Apply safely

1. Resolve the logical work and retain the raw input.
2. Search all configured identifiers and then normalized title/author across
   canonical records and import staging. Explain ambiguity instead of choosing
   a weak match.
3. Build a field-level plan classified as user-owned, curator-owned, or shared.
   On shared fields, follow the configured merge rule; absent a rule, preserve
   the existing non-empty value and propose the researched alternative.
4. In proposal mode, report the intended record, match evidence, sources,
   protected values, field changes, and review markers without writing. Apply
   when the user requested changes or approved the proposal.
5. Recheck the target and configuration immediately before applying. Make the
   smallest idempotent create or update, preserve all protected content, and
   record supported provenance and research timestamps.
6. Do not delete ordinary records merely because interest changed. Use the
   configured dropped or abandoned state and decision reason. Limit deletion
   to confirmed duplicates, erroneous imports, malformed records, or an
   explicit request, with normal approval boundaries.

The deterministic helper in `scripts/book_records.py` provides reusable
configuration discovery, normalization, duplicate matching, import planning,
and protected merge primitives. It is not a KB writer and does not replace
inspection of the configured schema or existing records.

## Validate and report

Before finishing, inspect the complete diff and status. Verify the configuration
used, template conformance, protected-field preservation, duplicate search,
logical-work policy, valid controlled values, source-to-claim support,
source-specific ratings, timestamps, links and paths, review markers, and
idempotency. Search changed files for secrets, personal data, and machine-local
configuration. Run repository validation and `git diff --check`; never claim a
check ran when it did not.

Report records created or updated, duplicate decisions and evidence, protected
content retained, provenance and freshness dates, skipped or unresolved data,
validation performed, and uncommitted changes.
