# filename: my_tests.py
import unittest

def all_prefixes(string: str) -> list:
    if len(string) == 0:
        return []
    elif len(string) == 1:
        return ["", string]

    current_prefix = string[0]
    result = [current_prefix] + all_prefixes(string[1:])
    return result

class TestsAllPrefixes(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(all_prefixes(""), [])

    def test_single_character(self):
        self.assertEqual(all_prefixes("a"), ["", "a"])

    def test_multiple_characters(self):
        self.assertEqual(all_prefixes("abc"), ["", "a", "ab", "ac", "abc"])

if __name__ == "__main__":
    unittest.main()