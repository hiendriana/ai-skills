---
name: snowboard-curator
description: Research a specific snowboard model and season, create or update a sourced board report, and add a personal sizing and on-snow test plan when testing is requested. Use for snowboard specifications, reviews, and board research; follow the destination repository's ownership and template rules when saving notes.
---

# Snowboard Curator

Research a snowboard without conflating model years, reviewer opinions, and the rider's own experience. Use [the report template](templates/board-research.md) for a new standalone report; adapt it to an existing destination note rather than replacing that note's structure.

## Choose the output

- For research alone, produce the core report. Add personal sizing and a test plan only when the user asks to test the board or otherwise requests test planning. Do not add empty test sections to research-only reports.
- When the user names an existing report, inspect and update it in place. Preserve personal notes, tested sizes, impressions, attribution, and useful links. Check for an existing board page before creating another.
- When saving to a repository, read its `AGENTS.md`, relevant README files, and templates first. Let that repository choose the location, naming, index updates, specification ownership, and lifecycle. If no destination policy exists, return the report in chat or use a destination the user gives; do not invent a permanent hierarchy.
- Preserve unrelated changes. Do not commit or publish unless requested.

## Research the exact board

1. Establish manufacturer, model, edition or variant, and the season/model year being researched. Ask for clarification if multiple materially different boards match and the intended one cannot be inferred.
2. Find the manufacturer's page for that exact board and season. Give the direct product or archived manufacturer link when available. If the current page covers another season, say so.
3. Extract the manufacturer's complete available size chart for the identified season into the report. Include recommended rider weight for every size when published, plus the other supplied dimensions and fit fields useful for comparing sizes. Keep units and exact size labels, including wide or other variants. Mark unavailable values as unreported; never fill gaps from another season or retailer without clear attribution.
4. Label the table's season, source, and date checked. If a manufacturer changes its chart or sources conflict, identify which value came from which source and do not silently combine them.
5. Find substantive reviews for the same model and, where possible, the same season. Keep webpage reviews and videos in separate sections. Prioritize review outlets specified by the user or destination repository; otherwise seek independent reviews alongside the manufacturer description. Record each review's model year or uncertainty. Embed videos when the output format supports it, and always include a direct link.
6. Attribute review claims and distinguish consensus from disagreement. Turn the most relevant claims into concise things to pay attention to; do not present a reviewer's impression as the rider's own finding. Keep a notes area for the rider without inventing observations.

## Add a test plan when requested

- Read available rider context and prior board notes, or ask for the fit details needed to make a useful recommendation: rider weight, boot size, riding goals, and relevant tested boards or sizes. Do not infer missing measurements or riding impressions.
- Recommend the first size to try, explain the manufacturer weight and boot guidance and the size tradeoffs, and label uncertainty. Add an alternative only when there is a useful reason to compare it. If essential context or reliable season-specific sizing is missing, state what is needed instead of guessing a precise size.
- Keep sizes already tested, sizes the rider already intends to test, and the new recommendation distinct. Do not replace an existing plan merely because the recommendation differs.
- State the comparison purpose and a few observable questions for each proposed size. Include a compact session record for date, conditions and terrain, setup, time ridden, impressions, comparison baseline, and confidence. Keep prior first-person observations separate from external reviews.

## Check the result

Verify that links resolve, sources actually support the adjacent facts, size rows all belong to the labeled season, and rider weight guidance is present or explicitly unavailable. For repository edits, inspect the diff and status, check relative links and required indexes, and preserve one clear owner for each board. Report the output location, sources and season used, unresolved discrepancies, and any information needed for a stronger size recommendation.
