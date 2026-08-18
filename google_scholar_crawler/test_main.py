import unittest

from main import parse_serpapi_payload


SCHOLAR_ID = "7ir2zYsAAAAJ"


def valid_payload() -> dict:
    return {
        "search_metadata": {"status": "Success"},
        "search_parameters": {
            "engine": "google_scholar_author",
            "author_id": SCHOLAR_ID,
        },
        "author": {"name": "Zhen Sun"},
        "cited_by": {"table": [{"citations": {"all": 836}}]},
    }


class ParseSerpApiPayloadTests(unittest.TestCase):
    def test_parses_valid_payload(self) -> None:
        self.assertEqual(parse_serpapi_payload(valid_payload(), SCHOLAR_ID), ("Zhen Sun", 836))

    def test_rejects_wrong_profile(self) -> None:
        payload = valid_payload()
        payload["search_parameters"]["author_id"] = "wrong-id"
        with self.assertRaisesRegex(ValueError, "unexpected Scholar profile"):
            parse_serpapi_payload(payload, SCHOLAR_ID)

    def test_rejects_unsuccessful_search(self) -> None:
        payload = valid_payload()
        payload["search_metadata"]["status"] = "Processing"
        with self.assertRaisesRegex(ValueError, "did not complete"):
            parse_serpapi_payload(payload, SCHOLAR_ID)

    def test_rejects_missing_citation_count(self) -> None:
        payload = valid_payload()
        payload["cited_by"] = {"table": []}
        with self.assertRaisesRegex(ValueError, "citation count"):
            parse_serpapi_payload(payload, SCHOLAR_ID)

    def test_rejects_api_error_without_leaking_details(self) -> None:
        payload = valid_payload()
        payload["error"] = "Invalid API key: secret-value"
        with self.assertRaisesRegex(ValueError, "SerpApi reported an error") as context:
            parse_serpapi_payload(payload, SCHOLAR_ID)
        self.assertNotIn("secret-value", str(context.exception))


if __name__ == "__main__":
    unittest.main()
