import unittest
from unittest.mock import patch

from take_a_break import is_valid_url, get_break_interval


class TestTakeABreak(unittest.TestCase):

    def test_valid_http_url(self):
        self.assertTrue(is_valid_url("http://example.com"))

    def test_valid_https_url(self):
        self.assertTrue(is_valid_url("https://www.google.com"))

    def test_invalid_url(self):
        self.assertFalse(is_valid_url("hello"))

    def test_url_without_scheme(self):
        self.assertFalse(is_valid_url("www.google.com"))

    def test_empty_url(self):
        self.assertFalse(is_valid_url(""))

    @patch("builtins.input", return_value="5")
    def test_break_interval(self, mock_input):
        self.assertEqual(get_break_interval(), 300)

    @patch("builtins.input", return_value="0")
    def test_invalid_break_interval(self, mock_input):
        mock_input.side_effect = ["0", "2"]
        self.assertEqual(get_break_interval(), 120)


if __name__ == "__main__":
    unittest.main()
    