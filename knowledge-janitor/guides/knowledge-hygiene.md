# Knowledge Hygiene

Audit ownership, navigation, evidence, and maintainability without performing
normal knowledge curation.

## Structural checks

- Resolve relative Markdown links from their containing files, including
  anchors when practical.
- Report a navigation gap only when repository policy or structure establishes
  an expected owner or index and its relationship is missing or wrong. Name the
  page, expected owner/index, missing relationship, and evidence for it. Zero
  inbound links alone is not an issue.
- Compare domain and category indexes with actual pages.
- Identify duplicate topic owners, overlapping concepts and patterns, unclear
  page purposes, and thin pages that add navigation cost without durable value.
- Flag general pages dominated by project-specific implementation detail.
- Flag reusable knowledge apparently trapped in a primer, but route extraction
  to `knowledge-curator`; do not perform it here.

## Correctness and provenance

- Compare conflicting claims and preserve their scopes and uncertainty.
- Flag missing source links or provenance where a claim depends on external or
  repository evidence.
- Search for secrets, credentials, private endpoints, personal message content,
  sensitive identifiers, and obsolete machine-specific paths. Before reporting
  a sensitive-data, credential, privacy, or policy violation, inspect applicable
  repository policy for explicit exceptions. An approved value in its approved
  canonical location is not a violation; a copy elsewhere may still violate a
  location-specific exception. Do not treat an intact processed capture as
  ordinary durable knowledge.
- Use source dates, project references, and relevant Git history to identify
  drift risk. Age alone does not establish staleness; never invent current state.

Classify findings by evidence:

- `confirmed issue`: directly demonstrated, such as a broken link;
- `likely stale`: repository evidence supports likely drift;
- `needs source verification`: live or external authority is needed to assess
  current correctness;
- `organizational suggestion`: a maintainability improvement, not an error;
- `no action required`: reviewed and acceptable.

Do not merge, shorten, rename, or rewrite solely for stylistic consistency.
Recommend the smallest change that restores clear ownership or navigation.
