"""
This module contains unit tests for the functions in the scrabble_score module.
The tests cover the calculation of Scrabble scores, validation of word length,
and checking if a word exists in the dictionary.
"""

import unittest
from scrabble_score import calculate_score, validate_word_length, is_valid_word


class TestScrabbleScore(unittest.TestCase):
    """
    Tests for the Scrabble score calculation functions.
    """

    def test_single_letter(self):
        """
        Test the score calculation for a single letter.
        """
        self.assertEqual(calculate_score('A'), 1)

    def test_word_lowercase(self):
        """
        Test the score calculation for a word in lowercase.
        """
        self.assertEqual(calculate_score('cabbage'), 14)

    def test_word_uppercase(self):
        """
        Test the score calculation for a word in uppercase.
        """
        self.assertEqual(calculate_score('CABbAge'), 14)

    def test_invalid_input(self):
        """
        Test the score calculation for invalid(non-alphabetic) inputs.
        """
        with self.assertRaises(ValueError):
            calculate_score('cab123')


class TestScrabbleWordLength(unittest.TestCase):
    """
    Tests for validating word length.
    """

    def test_valid_length(self):
        """
        Test validation for a word with the correct length.
        """
        self.assertTrue(validate_word_length('hello', 5))

    def test_invalid_length(self):
        """
        Test validation for a word with an incorrect length.
        """
        self.assertFalse(validate_word_length('hello', 6))


class TestScrabbleDictionary(unittest.TestCase):
    """
    Tests for checking word validity against the dictionary.
    """

    def test_valid_word(self):
        """
        Test if a word is considered valid.
        """
        self.assertTrue(is_valid_word('hello'))

    def test_invalid_word(self):
        """
        Test if a word is considered invalid.
        """
        self.assertFalse(is_valid_word('xyzzy'))


if __name__ == '__main__':
    unittest.main()
