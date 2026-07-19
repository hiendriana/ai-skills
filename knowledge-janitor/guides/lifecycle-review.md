# Lifecycle Review

Review capture state without curating the captured knowledge.

## Eligible states

- Inspect `processed`, `rejected`, and `needs-review` notes for metadata and
  maintenance problems.
- Inspect archived notes when an archive already exists.
- Protect `pending` notes from archival, deletion proposals, status changes,
  and obsolescence judgments.

Check that lifecycle metadata uses understood statuses, preserves capture and
source metadata, records valid repository-relative destinations where
applicable, and does not claim a processing or archive commit that lacks the
change.

## Conservative archive eligibility

A processed note may be proposed for archival only when all of these are true:

- every recorded destination exists;
- integration appears complete without extracting new knowledge from the note;
- no unresolved conflict or question remains;
- no manual review is required;
- source metadata and original captured content remain intact;
- moving the note will not break links, or affected links can be updated;
- the note need not remain immediately accessible for likely reprocessing;
- the user has approved an archive policy.

A status of `processed`, age, duplication, or rejection is never sufficient by
itself. When evidence is incomplete, classify the note as not safe to archive
and explain what must be verified.

## Approved archive moves

Move only exact approved paths into `inbox/archive/`. Preserve filenames unless
a collision requires a non-destructive resolution. Preserve all existing front
matter and body content; add only lifecycle fields such as:

```yaml
archived_at: 2026-07-19
previous_path: inbox/example.md
```

Update references affected by the move and report old and new paths. Do not
create deeper archive taxonomies without an established repository convention.
