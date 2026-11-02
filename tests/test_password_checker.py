"""
Unit tests for password_checker.py
Only dummy passwords are used here. Never put real passwords in tests.

Run from the project folder with:
    python -m unittest discover tests
"""

import os
import sys
import unittest

# Let the tests find password_checker.py in the parent folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import password_checker as pc


class TestCharacterChecks(unittest.TestCase):

    def test_lowercase(self):
        self.assertTrue(pc.has_lowercase("abcDEF"))
        self.assertFalse(pc.has_lowercase("ABC123"))

    def test_uppercase(self):
        self.assertTrue(pc.has_uppercase("abcDEF"))
        self.assertFalse(pc.has_uppercase("abc123"))

    def test_number(self):
        self.assertTrue(pc.has_number("abc1"))
        self.assertFalse(pc.has_number("abcdef"))

    def test_special(self):
        self.assertTrue(pc.has_special("abc!"))
        self.assertFalse(pc.has_special("abc123"))

    def test_empty_string(self):
        self.assertFalse(pc.has_lowercase(""))
        self.assertFalse(pc.has_uppercase(""))
        self.assertFalse(pc.has_number(""))
        self.assertFalse(pc.has_special(""))


class TestLength(unittest.TestCase):

    def test_short(self):
        result = pc.check_length("abc")
        self.assertFalse(result["min"])
        self.assertFalse(result["good"])
        self.assertFalse(result["great"])

    def test_eight(self):
        result = pc.check_length("a" * 8)
        self.assertTrue(result["min"])
        self.assertFalse(result["good"])

    def test_twelve(self):
        result = pc.check_length("a" * 12)
        self.assertTrue(result["good"])
        self.assertFalse(result["great"])

    def test_sixteen(self):
        result = pc.check_length("a" * 16)
        self.assertTrue(result["great"])


class TestCommonPasswords(unittest.TestCase):

    def test_common(self):
        self.assertTrue(pc.is_common_password("password"))

    def test_common_uppercase(self):
        self.assertTrue(pc.is_common_password("PASSWORD"))

    def test_not_common(self):
        self.assertFalse(pc.is_common_password("xK9#mP2$vL7!qR4z"))


class TestScoringAndRating(unittest.TestCase):

    def test_empty_password_score(self):
        # Empty is "not common", so it only gets the +1 for that
        self.assertEqual(pc.calculate_score(""), 1)

    def test_full_score(self):
        self.assertEqual(pc.calculate_score("Dummy-Pass-Phrase-99!"), 8)

    def test_rating_ranges(self):
        self.assertEqual(pc.get_rating(3, False), "Weak")
        self.assertEqual(pc.get_rating(4, False), "Moderate")
        self.assertEqual(pc.get_rating(5, False), "Moderate")
        self.assertEqual(pc.get_rating(6, False), "Strong")
        self.assertEqual(pc.get_rating(7, False), "Strong")
        self.assertEqual(pc.get_rating(8, False), "Very Strong")

    def test_common_is_always_weak(self):
        self.assertEqual(pc.get_rating(8, True), "Weak")

    def test_hello123_is_weak(self):
        results = pc.check_password("hello123")
        self.assertEqual(results["rating"], "Weak")

    def test_strong_passphrase(self):
        results = pc.check_password("Dummy-Pass-Phrase-99!")
        self.assertEqual(results["rating"], "Very Strong")


class TestSuggestions(unittest.TestCase):

    def test_short_password_gets_length_tip(self):
        tips = pc.get_suggestions("abc")
        self.assertTrue(any("length" in tip for tip in tips))

    def test_suggestions_never_empty(self):
        tips = pc.get_suggestions("Dummy-Pass-Phrase-99!")
        self.assertTrue(len(tips) > 0)


if __name__ == "__main__":
    unittest.main()
