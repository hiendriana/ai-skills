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
An untracked or never-committed processed capture is a lifecycle and provenance
anomaly requiring review. Do not propose simply adding and committing it as a
repair; that action does not establish the missing integration or lifecycle
evidence.

An intact capture in a documented `processed/` recycle bin is immutable
historical provenance while retained. Do not propose rewriting or redacting it
because its contents would be unsuitable for ordinary durable knowledge.
Sensitive content alone is not a reason to change that processed copy. Report
an applicable policy requirement for earlier action if one exists; otherwise
prefer the normal lifecycle removal workflow.

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
- every `integrated_into` value resolves under applicable repository policy or
  an evidenced historical convention to an existing destination, directly or
  through a verified later move of that destination;
- comparison with the destination content verifies that useful durable
  knowledge was integrated, without new extraction or curation;
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
Immediately before classifying any capture eligible, repeat the inbound-link
search for its exact path and, for bundles, every member and the directory.
Previous repository evidence of an inbound dependency blocks eligibility until
that dependency is resolved and the current link search is clear. Any current
inbound link blocks eligibility, even if an earlier check found none.

Status, age, apparent duplication, or a populated `processing_commit` field is
never sufficient by itself. Verify the referenced commit and its relevant
contents. When any evidence is missing, classify the capture as ineligible and
state every failed gate and its exact evidence. Count a capture once in the
unique blocked total even when several gates fail.

## Destination evidence

Do not assume `integrated_into` is relative to the capture directory or apply
the current preferred prefix to historical values. Determine path semantics
from repository policy and, where policy permits, resolvable sibling captures
and historical usage. Record the rule and evidence used. Distinguish an invalid
or unresolvable value from an older valid value and from a resolvable value
that merely differs from today's preferred convention. A missing `vault/` or
other current prefix alone proves none of these. If multiple interpretations
remain possible, block removal for ambiguous destination metadata.

For example, if policy or consistent historical records establish that
`Notes/Topic.md` resolves from a former content root and that destination
exists, record that convention and review its content; do not label the path
invalid merely because newer captures use `vault/Notes/Topic.md`.

If a destination was moved after the capture was processed, trace the recorded
path through committed Git history to the current file and corroborate its
identity and content. Record the original value, the resolved historical path,
the move evidence, and the current repository-relative path separately. A
matching title, similar content, or guessed rename is insufficient. If the
chain is missing or ambiguous, block removal for unresolved destination
evidence. A literal link to the old path may remain broken; it does not by
itself require the old path to exist when the move and current integration are
proven. Preserve the processed capture's original provenance rather than
rewriting its historical link solely to pass eligibility.

Existence alone does not prove integration. Inspect each current destination
against the processed record sufficiently to establish that its useful durable
knowledge is present and that no unresolved question, conflict, review, or
provenance issue remains. If this would require new extraction, interpretation,
or curation, block removal and route it to `knowledge-curator`. A metadata
correction may be proposed only when the actual durable destination already
exists and evidence identifies it. Never create a missing note or synthesize
content to satisfy an eligibility gate. If durable content is missing or
incomplete, classify the capture as blocked and route the work to
`knowledge-curator`; do not propose a new destination page or other durable
knowledge as a janitor repair.

## Review and approval sequence

1. Report each exact candidate path, `status: processed`, lifecycle dates,
   elapsed retention, every recorded destination, its resolved historical and
   current paths when moved, move and integration evidence, unresolved issues,
   inbound links, tracking, working tree and index state, and the commit
   identifier and exact processed path that prove recovery.
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
