---
name: knowledge-janitor
description: Audit lifecycle state and hygiene in personal Markdown knowledge repositories with top-level inboxes and multiple domains. Use when Codex is asked to review processed, rejected, needs-review, or archived captures; find broken links, stale indexes, duplication, drift, metadata defects, provenance gaps, or sensitive values; propose conservative archival or cleanup; or apply an explicitly approved archive or hygiene plan without curating pending knowledge.
---

# Knowledge Janitor

Review capture lifecycle and knowledge-base hygiene. Propose safe maintenance
before changing anything.

## Boundaries

- Do not curate pending captures, extract new concepts from them, or integrate
  their content into domain pages. Use `knowledge-curator` for that work.
- Do not maintain documentation inside source software repositories. Use
  `repository-documentation-audit` for that work.
- Do not infer permission to change files from a general cleanup request.
- Never use `rm`, `git clean`, destructive glob deletion, permanent filesystem
  deletion, or history-rewriting Git commands.
- Never archive, move, delete, merge, rename, rewrite, or change status without
  the mode-specific explicit approval defined below.

Read [lifecycle review](guides/lifecycle-review.md), [knowledge hygiene](guides/knowledge-hygiene.md),
and [safety and validation](guides/safety-and-validation.md) before proposing or
applying the corresponding work.

## Establish scope

1. Locate the repository root and read applicable `AGENTS.md`, the root
   `README.md`, domain indexes, and `inbox/README.md` when present.
2. Inspect Git status and preserve unrelated changes.
3. Inspect only the requested scope. A full audit may include processed,
   rejected, and `needs-review` inbox notes; an existing archive; domain
   indexes; project primers; concepts; patterns; technologies; runbooks;
   decisions; glossary pages; relative Markdown links; and relevant Git
   history.
4. Treat pending notes as protected provenance. Do not assess their knowledge
   for integration, mark them obsolete, archive them, or propose deleting them.

## Select a mode

### Audit mode — default

Inspect and report only. Do not modify files, statuses, links, content, paths,
or Git history. A request to audit, review, clean up, tidy, or run the janitor
selects audit mode unless it explicitly approves named actions.

### Apply approved archive plan

Move only explicitly named, previously reviewed notes from `inbox/` to
`inbox/archive/`. Preserve content, front matter, filename, provenance, and Git
history where possible. Add `archived_at` and, when useful, `previous_path`;
update only links that the move would otherwise break. Resolve collisions
safely and do not invent date-based folders without an existing convention.

Archive eligibility is necessary but not sufficient: the user must also have
approved the repository's archive policy and the exact notes in the plan.

### Apply approved hygiene plan

Apply only named page merges, renames, link fixes, index updates, metadata
repairs, or content removals that were previously proposed and explicitly
approved. Preserve meaning and provenance. Make no adjacent stylistic or
organizational changes.

### Deletion review

Produce proposals only. Run this mode only when the user explicitly asks for a
deletion review. Name each candidate, explain redundancy and the knowledge or
provenance that would be lost, and require later file-specific approval.

Even after approval, never permanently delete a capture. Use a repository's
explicitly documented recoverable removal mechanism if one exists; otherwise
report that deletion cannot be performed by this skill. Prefer keeping or
archiving over removal.

## Audit lifecycle and hygiene

For processed and rejected notes, verify lifecycle metadata, recorded
destinations, unresolved questions, understandable provenance, link effects,
and future reprocessing value. A `processed` status alone never establishes
archive eligibility. Apply the conservative criteria in the lifecycle guide.

Audit durable knowledge for broken relative links, orphaned substantive pages,
duplicate ownership, overlapping concepts and patterns, stale indexes,
inconsistent terminology, unclear purpose, misplaced project detail, trapped
general knowledge, unjustifiably thin pages, conflicting claims, missing
provenance, sensitive values, obsolete local paths, and invalid lifecycle
metadata. Do not rewrite for stylistic preference.

Use recorded sources, dates, project references, and relevant Git history to
assess drift. Do not call a page outdated without evidence. Classify findings
as `confirmed issue`, `likely stale`, `needs source verification`,
`organizational suggestion`, or `no action required` when useful.

## Report

In audit mode, report:

1. repository areas inspected;
2. processed notes reviewed;
3. notes eligible for possible archival;
4. notes not safe to archive and why;
5. invalid or incomplete lifecycle metadata;
6. broken links;
7. orphaned pages;
8. duplication or overlapping ownership;
9. stale or drift-sensitive claims;
10. sensitive-information findings;
11. proposed actions ordered by risk;
12. actions requiring explicit approval;
13. items requiring source verification.

In an apply mode, additionally report exact files moved and modified, metadata
changes, links updated, proposed actions intentionally not applied, and every
validation result.

Do not claim a check passed unless it was run.
