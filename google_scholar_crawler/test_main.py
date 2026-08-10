import unittest

from main import parse_profile_html


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


if __name__ == "__main__":
    unittest.main()
