import tempfile
import unittest
from pathlib import Path

from book_records import (discover_config, enrichment_profile, find_duplicates,
                          import_key, merge_research, plan_lazy_import,
                          reader_rating, semantic_state)


class BookRecordsTests(unittest.TestCase):
    def test_config_discovery_and_explicit_precedence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "config").mkdir()
            conventional = root / "config/book-curator.json"
            conventional.write_text("{}", encoding="utf-8")
            explicit = root / "books.yaml"
            explicit.write_text("schema: 1\n", encoding="utf-8")
            self.assertEqual(discover_config(root), conventional)
            self.assertEqual(discover_config(root, Path("books.yaml")), explicit)

    def test_protected_fields_survive_refresh(self):
        old = {"status": "reading", "priority": 5, "summary": "old", "my_notes": "keep"}
        new = {"status": "read", "priority": 1, "summary": "new", "my_notes": "replace"}
        merged = merge_research(old, new, user_owned={"status", "priority", "my_notes"}, curator_owned=new)
        self.assertEqual(merged, {"status": "reading", "priority": 5, "summary": "new", "my_notes": "keep"})

    def test_import_is_idempotent_and_lazy(self):
        source = {"provider": "Goodreads", "source_id": "7", "title": "Dune", "author": "Frank Herbert", "priority": 5}
        planned = plan_lazy_import([source, dict(source)], review_value="review")
        self.assertEqual(len(planned), 1)
        self.assertEqual(planned[0]["enrichment"], "deferred")
        self.assertNotIn("priority", planned[0])
        self.assertEqual(import_key(source), ("source", "goodreads", "7"))

    def test_import_deduplicates_providers_by_book_identity(self):
        goodreads = {"provider": "Goodreads", "source_id": "7", "title": "Dune", "author": "Frank Herbert", "isbn13": "9780441172719"}
        amazon = {"provider": "Amazon", "source_id": "B1", "title": "Dune", "author": "Frank Herbert", "isbn13": "978-0-441-17271-9"}
        self.assertEqual(len(plan_lazy_import([goodreads, amazon], review_value=True)), 1)

    def test_duplicate_by_isbn(self):
        existing = [{"title": "Other", "author": "A", "isbn13": "978-0-123456-47-2"}]
        matches = find_duplicates({"title": "Changed", "author": "B", "isbn13": "9780123456472"}, existing)
        self.assertEqual(matches[0]["matched_by"], ["isbn13"])

    def test_duplicate_by_normalized_title_author(self):
        existing = [{"title": "The Left Hand of Darkness", "author": "Ursula K. Le Guin"}]
        matches = find_duplicates({"title": "the left-hand of darkness", "author": "URSULA K LE GUIN"}, existing)
        self.assertEqual(matches[0]["matched_by"], ["title_author"])

    def test_one_logical_book_ignores_edition_without_identity_match(self):
        existing = [{"title": "Dune", "author": "Frank Herbert", "edition_year": 1965}]
        candidate = {"title": "Dune", "author": "Frank Herbert", "edition_year": 2019}
        self.assertEqual(find_duplicates(candidate, existing)[0]["matched_by"], ["title_author"])

    def test_dropped_and_abandoned_remain_distinct(self):
        mapping = {"dropped": "not-for-me", "abandoned": "stopped-reading"}
        self.assertEqual(semantic_state("not-for-me", mapping), "dropped")
        self.assertEqual(semantic_state("stopped-reading", mapping), "abandoned")

    def test_fiction_and_nonfiction_routing(self):
        self.assertEqual(enrichment_profile("Fiction"), "fiction")
        self.assertEqual(enrichment_profile("non-fiction"), "nonfiction")

    def test_missing_external_rating_stays_source_specific(self):
        missing = reader_rating("Goodreads", None, None, "https://example.invalid/book", "2026-09-21")
        storygraph = reader_rating("StoryGraph", 4.2, 100, "https://example.invalid/sg", "2026-09-21")
        self.assertFalse(missing["available"])
        self.assertIsNone(missing["rating"])
        self.assertEqual(storygraph["rating"], 4.2)
        self.assertNotIn("combined", storygraph)

    def test_ambiguous_external_rating_is_not_accepted(self):
        rating = reader_rating("Goodreads", 4.5, 200, "https://example.invalid/book", "2026-09-21", issue="work match ambiguous")
        self.assertFalse(rating["available"])
        self.assertIsNone(rating["rating"])
        self.assertEqual(rating["issue"], "work match ambiguous")

    def test_provenance_is_preserved_during_refresh(self):
        provenance = [{"source_type": "person", "source_name": "Sam", "note": "Strong recommendation"}]
        existing = {"recommendation_provenance": provenance, "summary": "old"}
        researched = {"recommendation_provenance": [], "summary": "new"}
        merged = merge_research(existing, researched, user_owned={"recommendation_provenance"}, curator_owned=researched)
        self.assertEqual(merged["recommendation_provenance"], provenance)
        self.assertEqual(merged["summary"], "new")


if __name__ == "__main__":
    unittest.main()
