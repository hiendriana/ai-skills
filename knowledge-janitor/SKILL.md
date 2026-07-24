---
name: knowledge-janitor
description: Audit capture lifecycle and general hygiene in personal Markdown knowledge repositories, including active-inbox cleanup, processed recycle-bin review, and exact-file Git-recoverable removal after explicit approval. Use when Codex is asked to review processed, rejected, or needs-review captures; identify eligible removal candidates; find broken links, stale indexes, duplication, drift, metadata defects, provenance gaps, or sensitive values; or apply an explicitly approved recycle-bin removal or hygiene plan without curating pending knowledge.
---

# Knowledge Janitor

Audit capture lifecycle and repository hygiene. Propose safe maintenance before
changing anything.

## Boundaries

- Do not curate pending captures or integrate their content. Use
  `knowledge-curator` for that work.
- Do not maintain source-repository documentation. Use
  `repository-documentation-audit` for that work.
- Require repository policy that explicitly documents the `processed/`
  recycle-bin and recoverable removal workflow before moving or removing a
  capture.
- Treat a general cleanup request as audit/proposal mode, never removal approval.
- Never commit unless separately requested.
- Fail closed on ambiguous path scope, lifecycle state, Git evidence,
  destinations, integration, links, working-tree state, retention, or approval.

Read [lifecycle review](guides/lifecycle-review.md), [knowledge hygiene](guides/knowledge-hygiene.md),
and [safety and validation](guides/safety-and-validation.md) before proposing or
applying the corresponding work.

## Establish scope

1. Locate the repository root and read applicable `AGENTS.md`, root `README.md`,
   domain indexes, and inbox policy files.
2. Inspect Git status and preserve unrelated changes.
3. Confirm which directories repository policy defines as active capture
   inboxes and processed recycle bins.
4. Protect pending, `needs-review`, rejected, untracked, and never-committed
   captures from removal.

## Select a mode

### Active inbox cleanup

Audit active inboxes for captures already marked `processed` but misplaced
outside the documented recycle bin. Propose exact moves and repairs; do not move
anything without explicit approval and successful validation.

### Recycle-bin review

Audit entries under documented `processed/` capture directories. Verify the
eligibility gates in the lifecycle guide and report exact candidates before any
change. This is the default for requests to clean or review processed captures.

### Approved recycle-bin removal

Remove only exact files that passed a prior deletion review and then received
file-specific approval. Recheck every gate immediately before removal and use
only the repository's documented recoverable version-control workflow. Do not
commit unless separately requested.

### General knowledge hygiene

Audit or apply explicitly approved link, metadata, ownership, index,
duplication, or drift repairs unrelated to capture removal. Preserve meaning and
provenance; make no adjacent stylistic changes.

## Audit and propose

For processed captures, verify lifecycle metadata, destinations, integration
completeness, unresolved review or provenance issues, inbound links, retention
policy, Git tracking, commit evidence, and working-tree clarity. A `processed`
status or age alone never establishes eligibility.

Audit durable knowledge for broken links, orphaned pages, duplicate ownership,
stale indexes, conflicting claims, missing provenance, sensitive values,
obsolete paths, and invalid metadata. Do not rewrite for stylistic preference
or call content outdated without evidence.

## Report

In audit or review mode, report:

1. repository policy and areas inspected;
2. active-inbox lifecycle issues;
3. processed captures reviewed;
4. exact removal candidates and eligibility evidence;
5. captures ineligible for removal and failed gates;
6. retention findings;
7. lifecycle, link, ownership, drift, provenance, or sensitive-data findings;
8. proposed actions ordered by risk;
9. exact actions requiring explicit approval.

After approved removal, additionally report every removed path, its approval,
the commit evidence that preserves its contents, the documented workflow used,
all files modified, actions intentionally not applied, and every validation
result. Do not claim a check passed unless it ran.
