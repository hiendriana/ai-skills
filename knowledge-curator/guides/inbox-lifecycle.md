# Inbox Lifecycle

Use this lifecycle only when repository policy explicitly defines the active
inbox and its `processed/` directory. The processed directory is a temporary
recycle bin, not durable knowledge or proof of Git recoverability.

## Statuses and locations

- `pending`: captured but not safely integrated. Treat a capture without a
  status as pending; keep it in the active inbox.
- `processed`: approved knowledge was integrated, destinations were validated,
  lifecycle metadata was recorded, and the complete capture was moved to that
  inbox's `processed/` directory.
- `needs-review`: integration is blocked by evidence, ambiguity, contradiction,
  sensitive content, or a human decision; keep it in the active inbox.
- `rejected`: explicitly judged unsuitable for integration; set only with
  explicit authority and keep it in the active inbox unless repository policy
  defines a separate lifecycle outside this skill.

The curator never deletes a capture. A janitor may later review a committed
processed capture and remove it only under the repository's explicit policy and
file-specific approval.

## Front matter and content preservation

After successful integration and validation, update only lifecycle fields:

```yaml
---
status: processed
captured_at: 2026-07-19
source_type: chat
processed_at: 2026-07-24
integrated_into:
  - software/concepts/example.md
processing_commit:
---
```

Use repository-relative paths in `integrated_into`. Preserve all other front
matter, the complete body, source metadata, attribution, links, quotations, and
uncertainty while moving the file. Keep `processing_commit` empty or omit it
until a commit actually contains the processed capture and its integration; do
not predict a hash.

For `needs-review`, add only concise lifecycle metadata such as `review_reason`
when useful. Do not move it. For `rejected`, preserve the original rationale and
source material.

## Move and link rules

- Resolve the target from repository policy; do not assume every repository or
  every directory named `processed` implements this lifecycle.
- Move from an active inbox directly into that inbox's `processed/` directory,
  preserving the filename unless policy defines a collision rule.
- Stop safely on collisions or ambiguous source and destination paths.
- Update inbound links that would break. Prefer linking durable pages to durable
  owners rather than to a disposable processed capture.
- Validate integration before metadata and movement. If later steps fail, do
  not leave a capture falsely marked or located as processed.

## Git evidence and idempotency

Report these questions separately:

1. Is the processed path currently tracked by Git?
2. Does an existing commit contain the processed capture at that path and, when
   required by policy, the corresponding integration?

Use repository-relative exact paths and inspect Git's index and history. File
existence, a staged move, or a tracked path alone does not prove that a commit
contains the processed capture. Record a commit identifier only after verifying
its contents.

Skip processed captures during ordinary enumeration. On an explicit revisit,
verify every `integrated_into` destination and add only genuinely missing
knowledge. Never duplicate claims, repeat a completed move, or clear destination
history merely because another destination is added.
