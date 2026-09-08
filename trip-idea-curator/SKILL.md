---
name: trip-idea-curator
description: Research and organize outdoor route and trip ideas in Danny's knowledge base, including source verification, recommendation collections, duplicate detection, provenance, and placement in the Ideas-to-Completed lifecycle. Use for climbing, mountaineering, hiking, splitboarding, and related outdoor suggestions. Do not use for completed-tour records or generic inbox processing without a trip component.
---

# Trip Idea Curator

Turn links, captions, messages, rough route names, and collections of recommendations into concise, reviewable trip-idea notes. Preserve why an idea is interesting without presenting inspiration or historical reports as current safety information.

## Establish Repository Context

1. Locate the knowledge repository containing `Knowledge Base/Outdoors/Trips/README.md`.
2. Read the repository instructions, `Knowledge Base/README.md`, and the Trips README before proposing changes.
3. Inspect existing notes and indexes for the route, destination, spelling variants, and source links before creating anything.
4. Preserve unrelated working-tree changes. Do not commit unless the user explicitly asks.

If the input is an active inbox capture, use `knowledge-curator` when available for its proposal, integration, provenance, and processed-lifecycle workflow. This skill owns the trip-specific research and note shape; it does not independently mark or move inbox captures.

## Choose the Durable Owner

Use `Knowledge Base/Outdoors/Trips/` as the canonical owner:

- `Ideas/` for every trip that has not happened yet, from an unreviewed suggestion to a detailed plan with dates or reservations.
- `Completed/` only for completed-tour records; use the repository's completed-tour workflow instead of this skill.

Keep adding research and preparation to the note in `Ideas/`; planning detail is not a separate lifecycle state. Move the note to `Completed/` only after the trip happens. Activity-specific pages may index or link to the canonical note but must not copy its detail.

When several recommendations share a meaningful provenance, create a collection directory under `Ideas/`, such as `Route Suggestions from Jane Doe/`. Add a short `README.md` index and one Markdown file per distinct route or natural route combination. Merge multiple posts about the same route into one note while retaining every source.

Use title case with spaces for human-facing filenames and directories. Follow any stricter local naming convention already in the repository.

## Research and Assess

1. Identify the route precisely before writing. Keep ambiguous identifications explicit.
2. Search current sources for location, activity, difficulty, length or elevation, approach, descent, protection or equipment, season, access restrictions, and objective hazards when relevant.
3. Prefer official route databases, guidebook publishers, land managers, huts, rescue or avalanche services, and other first-party sources. Use detailed trip reports for attributed experience, not universal facts.
4. Distinguish verified route facts, statements attributed to the recommender or publisher, the user's personal assessment, and unresolved or time-sensitive information.
5. Treat historical posts, condition reports, grades, protection descriptions, and access details as planning context. State what needs current local verification.
6. Never infer suitability, safety, or equipment requirements from sparse social-media material.

Browse whenever current conditions, restrictions, route details, or recommendations could have changed. Link directly to useful sources and include access dates when the information is time-sensitive.

## Write the Notes

Follow [the route-note schema](references/route-note-schema.md), adapting sections to the activity. Keep the result useful for quick review on a phone:

- put identity and decision-relevant facts first;
- record `Suggested by` separately from the route publisher or inspiration source;
- preserve original links and attribution;
- use `Unknown` or a clear verification gap instead of filling missing facts;
- omit empty boilerplate sections;
- do not add a task list or planning checklist unless the user explicitly requests one.

For skiing or splitboarding ideas adapted from ski itineraries, label the adaptation and leave terrain suitability, transitions, exit options, and current avalanche conditions as explicit review items unless verified.

## Update Navigation and Validate

Update the Trips index and only the relevant activity index or collection README. Keep one detailed owner and link elsewhere.

Before finishing:

1. Inspect the final diff and working-tree status.
2. Verify relative links and referenced paths.
3. Confirm that each route has one canonical note.
4. Check that sources support the stated facts and that uncertainty remains visible.
5. Confirm no private values, credentials, duplicated detail, or placeholder pages were introduced.
6. Report what was created or changed, what remains uncertain, and whether anything was intentionally left uncommitted.
