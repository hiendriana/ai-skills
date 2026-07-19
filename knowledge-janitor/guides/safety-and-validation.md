# Safety and Validation

Keep audits read-only and apply runs narrowly authorized.

## Approval boundary

- Audit mode is always the default.
- Archive apply mode requires an approved archive policy and exact note paths.
- Hygiene apply mode requires exact named actions or files from a reviewed
  proposal.
- Deletion review does not authorize deletion. Later approval must name every
  file, and this skill still may not perform permanent deletion.
- A general instruction to clean, tidy, organize, fix everything, or apply best
  judgment is not approval for moves or content changes.

Before applying, recheck Git status, current paths, lifecycle metadata, links,
and the approved target list. Stop if repository state invalidates the plan.

## Prohibited operations

Never use `rm`, `git clean`, destructive glob deletion, permanent filesystem
deletion, `git reset --hard`, rebase, filter-branch, filter-repo, or other
history-rewriting commands. Do not remove pending, processed, rejected, or
archived captures as an incidental cleanup step.

## Apply validation

After an approved change:

1. confirm every moved or modified file is on the approved list;
2. verify source captures retain their original content and provenance;
3. resolve modified relative links and referenced paths;
4. confirm archive metadata and destination paths are accurate;
5. check indexes and inbound links affected by moves or renames;
6. inspect the complete diff and working-tree status;
7. run `git diff --check` when the repository uses Git;
8. scan changes for sensitive values, unsupported claims, and unrelated edits;
9. report approved actions intentionally left unapplied.

Do not commit unless the user separately requests a commit.
