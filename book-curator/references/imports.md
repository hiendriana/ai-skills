# Imports and lazy enrichment

Service-specific export acquisition, authenticated APIs, and scraping remain
outside the core skill. Never request Goodreads or Amazon credentials merely to
process an export.

## Normalized import record

Normalize available input into:

- provider/source;
- provider source ID and URL;
- source-added date;
- title and author;
- ISBN/ISBN-13;
- ASIN;
- Goodreads ID;
- raw source reference or provenance pointer.

Retain unknown values as empty and preserve provider-specific extras only when
the KB contract provides a destination.

## Idempotent processing

Build a stable import key from provider plus source ID when present. Then match
canonical and staged records by stable book identifiers, followed by normalized
title and author. Re-importing the same provider item updates or skips its
existing representation; it must not create another record or duplicate a
provenance event.

If identifiers disagree or fallback matching produces multiple candidates,
retain the normalized item with the raw input and configured review marker. Do
not guess, merge, or discard it.

## Lazy default

Unless authoritative configuration says otherwise, bulk import means:

1. normalize;
2. deduplicate;
3. create or update a lightweight candidate record;
4. set the configured needs-review marker;
5. preserve import provenance;
6. leave personal priority/rating and other user-owned fields untouched;
7. skip full web research.

Fully enrich only when the user reviews or shortlists the item, explicitly asks
for enrichment, or the KB's lazy-enrichment policy requires it.
