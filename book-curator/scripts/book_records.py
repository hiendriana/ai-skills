#!/usr/bin/env python3
"""Deterministic primitives for generic book-curation workflows.

This module deliberately performs no network access and writes no KB files.
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Any, Iterable, Mapping


CONFIG_CANDIDATES = (
    "book-curator.yaml", "book-curator.yml", "book-curator.json",
    ".book-curator.yaml", ".book-curator.yml", ".book-curator.json",
    "config/book-curator.yaml", "config/book-curator.yml", "config/book-curator.json",
)
STABLE_IDS = ("isbn13", "goodreads_id", "asin")


def discover_config(root: Path, explicit: Path | None = None) -> Path | None:
    """Return an explicit or conventional repository-local config path."""
    root = root.resolve()
    if explicit is not None:
        candidate = explicit if explicit.is_absolute() else root / explicit
        candidate = candidate.resolve()
        try:
            candidate.relative_to(root)
        except ValueError as exc:
            raise ValueError("book configuration must be inside the KB root") from exc
        if not candidate.is_file():
            raise FileNotFoundError(candidate)
        return candidate
    for relative in CONFIG_CANDIDATES:
        candidate = root / relative
        if candidate.is_file():
            return candidate
    return None


def normalize_text(value: str | None) -> str:
    """Normalize text conservatively for fallback matching."""
    if not value:
        return ""
    value = unicodedata.normalize("NFKC", value).casefold()
    value = re.sub(r"[^\w]+", " ", value, flags=re.UNICODE)
    return " ".join(value.split())


def normalize_isbn(value: str | None) -> str | None:
    """Strip ISBN punctuation and reject values with an invalid shape."""
    if not value:
        return None
    normalized = re.sub(r"[^0-9Xx]", "", value).upper()
    if re.fullmatch(r"\d{13}", normalized) or re.fullmatch(r"\d{9}[\dX]", normalized):
        return normalized
    return None


def normalized_record(record: Mapping[str, Any]) -> dict[str, Any]:
    result = dict(record)
    isbn = normalize_isbn(str(record.get("isbn13") or record.get("isbn") or ""))
    if isbn:
        result["isbn13" if len(isbn) == 13 else "isbn"] = isbn
    result["_title_key"] = normalize_text(_string(record.get("title")))
    result["_author_key"] = normalize_text(_string(record.get("author")))
    return result


def find_duplicates(candidate: Mapping[str, Any], records: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Return match evidence; identifiers outrank title/author fallback."""
    wanted = normalized_record(candidate)
    strong: list[dict[str, Any]] = []
    fallback: list[dict[str, Any]] = []
    for record in records:
        existing = normalized_record(record)
        matched_ids = [key for key in STABLE_IDS if wanted.get(key) and existing.get(key)
                       and str(wanted[key]).casefold() == str(existing[key]).casefold()]
        if matched_ids:
            strong.append({"record": record, "matched_by": matched_ids})
        elif (wanted["_title_key"] and wanted["_author_key"]
              and wanted["_title_key"] == existing["_title_key"]
              and wanted["_author_key"] == existing["_author_key"]):
            fallback.append({"record": record, "matched_by": ["title_author"]})
    return strong or fallback


def import_key(record: Mapping[str, Any]) -> tuple[str, ...]:
    provider = normalize_text(_string(record.get("source") or record.get("provider")))
    source_id = _string(record.get("source_id"))
    if provider and source_id:
        return ("source", provider, source_id.casefold())
    normalized = normalized_record(record)
    for key in STABLE_IDS:
        if normalized.get(key):
            return (key, str(normalized[key]).casefold())
    if normalized["_title_key"] and normalized["_author_key"]:
        return ("title_author", normalized["_title_key"], normalized["_author_key"])
    raise ValueError("import record lacks a stable ID or title and author")


def plan_lazy_import(records: Iterable[Mapping[str, Any]], *, review_value: Any) -> list[dict[str, Any]]:
    """Deduplicate normalized imports and mark lightweight records for review."""
    planned: dict[tuple[str, ...], dict[str, Any]] = {}
    for raw in records:
        key = import_key(raw)
        if key in planned:
            continue
        duplicate = find_duplicates(raw, planned.values())
        if duplicate:
            continue
        item = {name: value for name, value in normalized_record(raw).items() if not name.startswith("_")}
        item["needs_review"] = review_value
        item["enrichment"] = "deferred"
        for protected in ("priority", "personal_rating"):
            item.pop(protected, None)
        planned[key] = item
    return list(planned.values())


def merge_research(existing: Mapping[str, Any], researched: Mapping[str, Any], *,
                   user_owned: Iterable[str], curator_owned: Iterable[str]) -> dict[str, Any]:
    """Apply only curator-owned research and preserve every other existing field."""
    result = dict(existing)
    allowed = set(curator_owned) - set(user_owned)
    for key in allowed:
        if key in researched:
            result[key] = researched[key]
    return result


def semantic_state(value: str, mapping: Mapping[str, str]) -> str | None:
    """Map a configured value to a generic semantic state."""
    return {configured: semantic for semantic, configured in mapping.items()}.get(value)


def enrichment_profile(book_type: str) -> str:
    normalized = normalize_text(book_type).replace(" ", "")
    if normalized not in {"fiction", "nonfiction"}:
        raise ValueError("book type must resolve to fiction or nonfiction")
    return normalized


def reader_rating(source: str, rating: Any, count: Any, url: str | None,
                  researched_at: str, *, issue: str | None = None) -> dict[str, Any]:
    """Keep a source-specific rating complete or explicitly unavailable."""
    result = {"source": source, "researched_at": researched_at}
    if rating is None or issue:
        result.update({"rating": None, "rating_count": None, "source_url": url,
                       "available": False, "issue": issue})
    else:
        result.update({"rating": rating, "rating_count": count, "source_url": url, "available": True})
    return result


def _string(value: Any) -> str:
    return value if isinstance(value, str) else ""
