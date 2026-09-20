# Safety and Validation

Keep audits read-only and apply runs narrowly authorized.

## Audit reporting

Enumerate active captures, all processed captures, eligible candidates, unique
blocked captures, and bundles before computing totals. Reconcile those sets
with retention-, metadata-, destination-, and inbound-link-blocked counts and
hygiene findings. Gate counts may overlap across unique blocked captures.
For each blocked capture, list every failed gate with exact evidence; do not
use a bare "ineligible" label. If any total cannot be reconciled, mark the
audit incomplete instead of publishing inconsistent totals.
Use the finding classes `confirmed issue`, `likely stale`,
`needs source verification`, `organizational suggestion`, and
`no action required` consistently in findings and proposed actions. Carry the
exact audited path into each proposed action; do not reconstruct or substitute
a similar path.

Prefer validation that leaves the repository untouched throughout audit mode.
Run only checks relevant to the audit, not unrelated test suites merely because
they exist. Avoid commands that create `__pycache__`, `.pyc`, or other temporary
artifacts in the repository. If a necessary validation creates them, remove
only those known artifacts and report both creation and cleanup.

Before finishing audit mode, check and report whether the repository is
unchanged, the working tree and index were checked, no unrelated file was
created or changed, counts reconcile, every eligible removal passed every
applicable gate, blocked captures name failed gates, policy exceptions were
honored, processed provenance was not treated as ordinary durable knowledge,
and no destructive action occurred. Do not claim an unperformed check passed.
As a final consistency check, reconcile all counts; compare every
proposed-action path byte for byte with its finding; confirm no proposed action
creates or integrates durable knowledge or otherwise crosses into
`knowledge-curator` responsibility; confirm intentional template placeholders
are not called broken links; confirm no OCR, visual extraction, or source
extraction was performed merely for eligibility; and confirm every eligible
removal candidate has zero current inbound links. Block eligibility or mark the
audit incomplete when any check fails.

## Approval boundary

- Audit and proposal mode is always the default.
- Moving a misplaced processed capture requires an approved exact path and a
  repository-documented recycle-bin policy.
- Removal requires a completed deletion review followed by later file-specific
  approval for every exact path.
- Bundle removal requires approval for the manifest and every declared member;
  never infer approval for members from a directory name.
- Hygiene changes require exact named actions or files from a reviewed plan.
- A request to clean, tidy, organize, fix everything, or use best judgment never
  authorizes movement or removal.

Before applying, recheck Git status, paths, lifecycle metadata, destinations,
integration completeness, links, retention, commit evidence, and the approved
target list. Stop if repository state invalidates or obscures the plan.

## Removal mechanism

Use only the repository's documented recoverable version-control workflow. In
a Git repository, an explicitly documented workflow may use an exact-path form
such as `git rm -- path/to/capture.md`, but only for a single reviewed and
approved file or an explicit list of individually approved files.

Never use filesystem `rm`, destructive globs, recursive directory deletion,
`git clean`, broad pathspecs, `git reset --hard`, rebase, filter-branch,
filter-repo, or other history rewriting. Never remove an ineligible capture as
an incidental cleanup step. Do not commit unless separately requested.

After approved removal of every member of a reviewed bundle, permit only a
nonrecursive empty-directory operation on that exact bundle directory. Verify it
is empty immediately first; stop if it contains any entry. This cleanup removes
no capture data and does not replace exact-member approval.

## Final validation

After an approved move, removal, or hygiene change:

1. confirm every changed or removed path was explicitly approved and in scope;
2. verify lifecycle state, destination existence, integration completeness, and
   commit evidence for every removed capture;
3. resolve relative links and referenced paths and verify no inbound link broke;
4. inspect the complete diff and working-tree status, including staged and
   unstaged state;
5. run `git diff --check` when the repository uses Git;
6. scan changed and candidate tracked files for sensitive values, unsupported
   claims, personal data, and machine-specific configuration;
7. confirm no unrelated file or lifecycle state changed;
8. report the recovery commit and committed path for each removed capture;
9. report approved actions intentionally left unapplied and all uncertainty.

For a bundle, repeat membership, media-type, size, SHA-256, inbound-link,
tracking, and committed-history checks for every member and confirm no empty or
partial bundle remains.

Do not claim a check passed unless it was run.
