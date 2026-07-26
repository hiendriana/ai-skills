# Lifecycle Review

Review capture state without curating captured knowledge.

## Lifecycle areas

- **Active inbox cleanup:** find captures marked `processed` but misplaced in an
  active inbox. Propose exact moves into its documented `processed/` directory.
- **Recycle-bin review:** evaluate captures already inside a documented
  `processed/` directory for retention or removal eligibility.
- **Approved recycle-bin removal:** remove only exact eligible files after a
  deletion review and later file-specific approval.
- **General knowledge hygiene:** keep unrelated links, metadata, ownership, and
  duplication work separate from capture removal.

Protect pending, `needs-review`, rejected, untracked, and never-committed
captures from removal in every mode. Treat a manifested bundle as one capture
and apply every gate to every member.

## Policy and path gate

Before proposing a move or removal, verify that repository policy explicitly:

1. identifies the source as a capture inbox;
2. identifies that inbox's `processed/` directory as a temporary recycle bin;
3. defines a recoverable version-control removal workflow; and
4. defines any required retention period or retention evidence.

Do not invent a default retention period. If policy is absent, conflicting, or
ambiguous, audit and report only.

## Removal eligibility

A processed capture is eligible for a removal proposal only when every check
passes:

- the exact file is inside a repository-documented processed capture directory;
- lifecycle status is `processed`;
- every repository-relative `integrated_into` destination exists;
- destination review shows the selected integration is complete without
  extracting new knowledge from the capture;
- no unresolved conflict, question, manual review requirement, or provenance
  problem remains;
- no inbound repository link would break;
- the file is tracked by Git;
- Git history proves an existing commit contains the capture at the processed
  path, and any stronger repository requirement for integration commit evidence
  also passes;
- the index and working tree make the file's identity and proposed removal
  unambiguous; and
- any repository-defined retention period has elapsed.

For a bundle, the exact manifest and every declared source file must pass every
applicable check. One failed member makes the complete bundle ineligible.

Status, age, apparent duplication, or a populated `processing_commit` field is
never sufficient by itself. Verify the referenced commit and its relevant
contents. When any evidence is missing, classify the capture as ineligible and
state what must be resolved.

## Review and approval sequence

1. Report each exact candidate path, every eligibility result, retention result,
   inbound-link result, and the commit identifier and path that prove recovery.
2. Explain what provenance or reprocessing convenience removal will discard
   from the working tree.
3. Make no change during the deletion review.
4. Require a later approval naming each exact file, including every member of a
   bundle. Broad approval such as "clean my inbox" or a bundle directory alone
   is insufficient.
5. Immediately before removal, repeat all gates and stop if repository state or
   evidence changed.

## Recoverability evidence

Git recoverability requires proof from an existing commit, not merely a file in
`processed/`, a tracked index entry, a staged addition, or an unverified hash in
front matter. Record the verified commit identifier and repository-relative path
for each candidate and confirm the committed blob contains the capture expected
to be removed.

For a bundle, record this evidence for `capture.md` and every declared source
file at their exact processed paths.

Removal itself is a working-tree change until committed. Report that distinction
and never create the removal commit unless explicitly requested.
