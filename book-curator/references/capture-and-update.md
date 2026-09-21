# Capture and safe update

## Identification and duplicate search

Accept a title, author/title pair, ISBN, Amazon or Goodreads URL, another
book-related URL, inbox mention, or natural-language recommendation. Preserve
the original input and its surrounding recommendation context.

Resolve title, author, work identity, book type, and stable identifiers from
reliable sources. Normalize ISBNs by removing separators and validating the
10/13-character shape; compare ISBN-13 where conversion is reliable. Extract a
Goodreads ID or ASIN only when the URL or source establishes it.

Search in this order:

1. configured provider source ID;
2. ISBN-13, Goodreads ID, and ASIN;
3. normalized title plus author, accounting conservatively for punctuation,
   whitespace, and case;
4. possible alternate titles/translations, treated as ambiguous unless evidence
   establishes the same logical work.

Multiple identifier matches to different records are a conflict. Do not merge
or choose automatically. Retain the input, mark it for review using the KB's
mechanism, and explain the competing evidence.

## Update plan

Classify every existing and proposed field by configured ownership. Preserve
user-owned fields byte-for-byte where the storage format permits, including
notes, review, reading state, priority, personal rating, contexts, and decision
reason. Update curator-owned fields only from supported research. Merge shared
fields only under the configured rule.

General refreshes must not reset manual decisions. Preserve recommendation
provenance as append-only distinct events when the schema permits; deduplicate
the same source event instead of overwriting the original reason.

Track original year separately from edition year, and keep edition ISBN/page or
audiobook facts scoped to their edition. Do not create a second work record
solely because a different translation, format, or edition was found unless the
configured identity policy requires it.

Reading language describes the language actually read. Leave it empty until
known. Started and finished dates do not require live progress tracking; add
reread history or intent only when configured and evidenced.
