import unittest

from main import _normalise_author


SCHOLAR_ID = "7ir2zYsAAAAJ"


class NormaliseAuthorTests(unittest.TestCase):
    def test_normalises_valid_author(self) -> None:
        author = {
            "name": "Zhen Sun",
            "scholar_id": SCHOLAR_ID,
            "citedby": 836,
            "publications": [
                {"author_pub_id": "paper-1", "bib": {"title": "Paper One"}},
                {"bib": {"title": "Incomplete entry"}},
            ],
        }

        result = _normalise_author(author, SCHOLAR_ID)

        self.assertEqual(result["citedby"], 836)
        self.assertEqual(list(result["publications"]), ["paper-1"])
        self.assertEqual(result["source"], "SCHOLARLY_1_5_1")
        self.assertIn("updated", result)

    def test_accepts_publications_dictionary(self) -> None:
        author = {
            "scholar_id": SCHOLAR_ID,
            "citedby": 836,
            "publications": {"paper-1": {"author_pub_id": "paper-1"}},
        }

        result = _normalise_author(author, SCHOLAR_ID)

        self.assertIn("paper-1", result["publications"])

    def test_rejects_wrong_profile(self) -> None:
        author = {"scholar_id": "wrong-id", "citedby": 836, "publications": []}

        with self.assertRaisesRegex(ValueError, "expected"):
            _normalise_author(author, SCHOLAR_ID)

    def test_rejects_invalid_citation_count(self) -> None:
        author = {"scholar_id": SCHOLAR_ID, "citedby": "836", "publications": []}

        with self.assertRaisesRegex(ValueError, "Invalid citation count"):
            _normalise_author(author, SCHOLAR_ID)

    def test_rejects_invalid_publications(self) -> None:
        author = {"scholar_id": SCHOLAR_ID, "citedby": 836, "publications": "invalid"}

        with self.assertRaisesRegex(ValueError, "publications collection"):
            _normalise_author(author, SCHOLAR_ID)


if __name__ == "__main__":
    unittest.main()
