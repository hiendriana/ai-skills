# Knowledge Hygiene

Audit ownership, navigation, evidence, and maintainability without performing
normal knowledge curation.

## Structural checks

- Resolve relative Markdown links from their containing files, including
  anchors when practical.
- Find substantive pages with no useful inbound navigation.
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
  sensitive identifiers, and obsolete machine-specific paths.
- Use source dates, project references, and relevant Git history to identify
  drift risk.

Classify findings by evidence:

- `confirmed issue`: directly demonstrated, such as a broken link;
- `likely stale`: evidence suggests drift but current authority was not checked;
- `needs source verification`: correctness depends on an authoritative source;
- `organizational suggestion`: a maintainability improvement, not an error;
- `no action required`: reviewed and acceptable.

Do not merge, shorten, rename, or rewrite solely for stylistic consistency.
Recommend the smallest change that restores clear ownership or navigation.
