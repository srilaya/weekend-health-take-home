import unittest
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import find_words, can_form_word, build_frequency_map

class TestWordFinder(unittest.TestCase):
    
    def test_find_words_multiple_matches(self):
        # Given test cases 
        input_string = "ate"
        dictionary = ["ate", "eat", "tea", "dog", "do", "god", "goo", "go", "good"]
        result = find_words(input_string, dictionary)
        self.assertEqual(result, ["ate", "eat", "tea"])

        input_string = "oogd"
        dictionary = ["ate", "eat", "tea", "dog", "do", "god", "goo", "go", "good"]
        result = find_words(input_string, dictionary)
        self.assertEqual(result, ["dog", "do", "god", "goo", "go", "good"])

    def test_find_words_single_match(self):
        input_string = "hello"
        dictionary = ["hello", "world"]
        result = find_words(input_string, dictionary)
        self.assertEqual(result, ["hello"])

    def test_find_words_no_matches(self):
        input_string = "abcd"
        dictionary = ["hello", "world"]
        result = find_words(input_string, dictionary)
        self.assertEqual(result, [])

    def test_find_words_empty_string(self):
        input_string = ""
        dictionary = ["hello", "world"]
        result = find_words(input_string, dictionary)
        self.assertEqual(result, [])
    
    def test_can_form_word_true(self):
        word = "hello"
        letter_map = {"h": 1, "e": 1, "l": 2, "o": 1}
        result = can_form_word(word, letter_map)
        self.assertTrue(result)
    
    def test_can_form_word_false(self):
        word = "hello"
        letter_map = {"h": 1, "e": 1, "l": 1, "o": 1}
        result = can_form_word(word, letter_map)
        self.assertFalse(result)
    
    def test_build_frequency_map(self):
        input_string = "hello"
        expected_map = {"h": 1, "e": 1, "l": 2, "o": 1}
        result = build_frequency_map(input_string)
        self.assertEqual(result, expected_map)
    
    def test_build_frequency_map_empty_string(self):
        input_string = "   "
        result = build_frequency_map(input_string)
        self.assertEqual(result, {})
    
if __name__ == '__main__':
    unittest.main()