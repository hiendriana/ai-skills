# Knowledge-base configuration contract

The knowledge base owns representation; the skill owns book-domain behavior.
Configuration may be structured data or clearly documented repository policy,
but it must resolve the following before permanent records are written.

## Required contract

- Canonical book-record path and naming rules.
- Template or schema and mappings for fields the workflow will touch.
- Allowed reading-state values and their mapping to the semantic states
  `candidate`, `shortlist`, `reading`, `read`, `dropped`, and `abandoned`.
- Ownership of each field: `user`, `curator`, or `shared`, plus merge rules for
  shared fields.
- Logical-work policy: one work per record by default, or an explicit
  edition-per-record override.
- Review marker/state and how ambiguity is represented.

## Conditional contract

Resolve these when the workflow uses them:

- Template path, dashboard/index updates, and import staging paths.
- Priority and personal-rating scales; ownership formats; difficulty values;
  controlled genres; topic/context expansion rules; language representation.
- Mappings for title, author, book type, original and edition publication data,
  page count, audiobook duration, series/number, ISBN-13, Goodreads ID, ASIN,
  reading dates/history, reread intent, ownership/location/library references,
  personal fields, research prose, source-specific ratings, recommendation
  provenance, freshness, and curator version.
- Research depth, preferred bibliographic/editorial sources, reader-rating
  sources, source precedence, refresh interval/triggers, and whether lightweight
  records may be enriched automatically.
- Import provider mappings and the lazy-enrichment policy.

Paths are repository-relative unless repository policy explicitly says
otherwise. Do not encode application-specific UI syntax in the generic skill.

## Minimal bootstrap proposal

When no contract exists, propose only the unresolved decisions above. A useful
minimal bootstrap declares a records path, template/schema, semantic state
mapping, field ownership, review marker, logical-work policy, and lazy-import
policy. Offer example semantic fields without choosing filenames, taxonomies,
or controlled vocabulary for the repository. Apply a bootstrap only after the
user approves it.

Once repository configuration exists, it replaces all bootstrap expectations.
