# Inbox Lifecycle

Inbox notes are permanent provenance records. Processing changes their
lifecycle metadata, not their captured content or location.

## Statuses

- `pending`: captured but not yet safely integrated. Treat a note without a
  status as pending.
- `processed`: approved durable knowledge was integrated and the recorded
  destinations were validated.
- `needs-review`: integration is blocked by missing evidence, ambiguity,
  contradiction, sensitive content, or a decision requiring human judgment.
- `rejected`: explicitly judged unsuitable for integration. Set this only when
  the user approves rejection or the invocation explicitly permits it.

Processed and rejected notes remain in the inbox. Do not use status as a signal
to move, archive, prune, or delete a note.

## Front matter

Use a small YAML block at the beginning of a note:

```yaml
---
status: pending
captured_at: 2026-07-19
source_type: chat
---
```

After successful integration, update only lifecycle fields while preserving
all other front matter and the complete captured body:

```yaml
---
status: processed
captured_at: 2026-07-19
source_type: chat
processed_at: 2026-07-19
integrated_into:
  - software/concepts/example.md
processing_commit:
---
```

Use repository-relative paths in `integrated_into`. Keep `processing_commit`
empty or omit it until a commit actually contains both the integration and the
corresponding lifecycle update. Do not predict a future commit hash.

For `needs-review`, keep existing metadata and add only a concise lifecycle
field such as `review_reason` when it helps the next review. For `rejected`,
record the status without removing the original rationale or source material.

## Transitions and idempotency

- Missing status -> `pending` when metadata is first added.
- `pending` -> `processed` only after successful integration and validation.
- `pending` -> `needs-review` when safe integration is blocked.
- `needs-review` -> `processed` after the blocker is resolved and integration
  succeeds.
- Any status -> `rejected` only with explicit rejection authority.

Skip `processed` notes by default. When reprocessing is explicit, verify every
recorded destination first and integrate only genuinely missing knowledge.
Never clear prior destination history merely because another destination is
added.
