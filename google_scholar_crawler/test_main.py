import unittest

from main import parse_profile_html, parse_serpapi_payload


SCHOLAR_ID = "7ir2zYsAAAAJ"


class ParseProfileHtmlTests(unittest.TestCase):
    def test_reads_citation_count_from_description_and_stats(self) -> None:
        html = f"""
        <html><head>
          <link rel="canonical" href="https://scholar.google.com/citations?user={SCHOLAR_ID}&amp;hl=en">
          <meta name="description" content="Ph.D. Candidate - Cited by 1,234 - LLM security">
        </head><body>
          <div id="gsc_prf_in">Zhen Sun</div>
          <a class="gsc_rsb_std">1,234</a>
        </body></html>
        """

        self.assertEqual(parse_profile_html(html, SCHOLAR_ID), ("Zhen Sun", 1234))

    def test_uses_stats_when_description_is_missing(self) -> None:
        html = f"""
        <link rel="canonical" href="https://scholar.google.com/citations?user={SCHOLAR_ID}">
        <div id="gsc_prf_in">Zhen Sun</div>
        <a class="gsc_rsb_std">836</a>
        """

        self.assertEqual(parse_profile_html(html, SCHOLAR_ID), ("Zhen Sun", 836))

    def test_rejects_wrong_profile(self) -> None:
        html = """
        <link rel="canonical" href="https://scholar.google.com/citations?user=wrong-id">
        <meta name="description" content="Cited by 836">
        """

        with self.assertRaisesRegex(ValueError, "expected"):
            parse_profile_html(html, SCHOLAR_ID)

    def test_rejects_bot_check_page(self) -> None:
        with self.assertRaisesRegex(ValueError, "bot-check"):
            parse_profile_html("Please confirm you are not a robot", SCHOLAR_ID)

    def test_rejects_conflicting_counts(self) -> None:
        html = """
        <meta name="description" content="Cited by 836">
        <a class="gsc_rsb_std">835</a>
        """

        with self.assertRaisesRegex(ValueError, "conflicting"):
            parse_profile_html(html, SCHOLAR_ID)


class ParseSerpApiPayloadTests(unittest.TestCase):
    def valid_payload(self) -> dict:
        return {
            "search_metadata": {"status": "Success"},
            "search_parameters": {
                "engine": "google_scholar_author",
                "author_id": SCHOLAR_ID,
            },
            "author": {"name": "Zhen Sun"},
            "cited_by": {
                "table": [
                    {"citations": {"all": 836, "since_2021": 800}},
                    {"h_index": {"all": 12, "since_2021": 12}},
                ]
            },
        }

    def test_reads_author_and_citation_count(self) -> None:
        self.assertEqual(
            parse_serpapi_payload(self.valid_payload(), SCHOLAR_ID),
            ("Zhen Sun", 836),
        )

    def test_rejects_wrong_profile(self) -> None:
        payload = self.valid_payload()
        payload["search_parameters"]["author_id"] = "wrong-id"

        with self.assertRaisesRegex(ValueError, "expected"):
            parse_serpapi_payload(payload, SCHOLAR_ID)

    def test_rejects_unsuccessful_search(self) -> None:
        payload = self.valid_payload()
        payload["search_metadata"]["status"] = "Processing"

        with self.assertRaisesRegex(ValueError, "did not complete"):
            parse_serpapi_payload(payload, SCHOLAR_ID)

    def test_rejects_missing_citation_count(self) -> None:
        payload = self.valid_payload()
        payload["cited_by"]["table"] = []

        with self.assertRaisesRegex(ValueError, "citation"):
            parse_serpapi_payload(payload, SCHOLAR_ID)

    def test_rejects_api_error_without_leaking_credentials(self) -> None:
        payload = {"error": "Invalid API key"}

        with self.assertRaisesRegex(ValueError, "Invalid API key"):
            parse_serpapi_payload(payload, SCHOLAR_ID)


if __name__ == "__main__":
    unittest.main()
