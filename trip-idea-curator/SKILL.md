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
2. Search current sources for location, activity, difficulty, length or elevation, approach, descent, protection or equipment, season, access restrictions, objective hazards, and useful logistics when relevant. For climbing routes, always search for available topos.
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

Add a clear `Logistics` section when access information would help evaluate or execute the trip. Record the actual route start and end, useful ways to get there, parking or public-transport constraints, and return or shuttle needs. Include a direct Google Maps link to a verified trailhead, parking area, station, or other useful access point when available; label the point precisely and never substitute an imprecise search result for a confirmed location.

For every multiday trip, add an `Accommodation` section with a compact night-by-night overview. Include only accommodation that shapes the itinerary: mountain huts, bivouacs, camps, staged trailheads, or a necessary pre-route or post-route stay. Do not recommend a generic hotel in the valley merely because lodging exists. For a single-day trip, include accommodation only when it materially affects access, an alpine start, transport, or route timing.

For route-based ideas, add a `Navigation and Track` section that makes prior work visible. Record the track source page, any preserved original GPX, the selected navigation master, the track's intended scope, review state, download date, and known caveats. Omit the section for destination-only ideas until a route exists.

For climbing routes, add a `Topos` section whenever topos are available. Retain multiple useful versions and sort them newest first. For every entry, record the date and what that date represents, such as creation, publication, guidebook edition, upload, page update, or photo date. Do not present a webpage date as the topo's creation date. Identify the format and scope, including whether it is a line topo, photo topo, overview, guidebook page, or on-site reference. Compare meaningful differences in line, grades, protection, variants, and descent rather than silently choosing one version. If no topo is found, state that outcome and name the principal sources checked.

Use one owner for each kind of information:

- the trip note is the canonical research overview and links everything together;
- the user's dedicated Google Drive account archives selected original GPX files, PDFs, topos, and other source files;
- one selected service, normally Komoot or Outdooractive, owns the editable navigation route;
- Suunto and the watch are deployment targets, not durable archives.

Keep ordinary webpages as links in the note. Create a Google Drive route folder only when files are worth preserving. Use the same route name across systems, retain an original GPX unchanged, and do not maintain duplicate working routes in Komoot and Outdooractive without a specific reason. A source link is sufficient for an early idea; archive the GPX when the route becomes a serious candidate, offline recovery matters, or the source is fragile. Archive downloadable topo files under the route's source archive when lawful and useful for personal offline reference; otherwise retain the topo page link. Record stable research once and refresh only time-sensitive conditions, access, restrictions, transport, and accommodation before the trip.

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
