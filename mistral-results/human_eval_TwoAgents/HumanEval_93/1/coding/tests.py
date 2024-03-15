# filename: tests.py
__all__ = ['run_tests']
import unittest, sys, os
sys.path.append(os.getcwd())
from complete_code import encode as encoder

class TestEncode(unittest.TestCase):
    def test_encode_empty_string(self):
        self.assertEqual('', encoder(''))
        
    def test_encode_single_letter(self):
        self.assertEqual('r', encoder('a'))
        
    def test_encode_single_digit(self):
        self.assertEqual('47S', encoder('1'))
        
    def test_encode_space(self):
        self.assertEqual(' SS', encoder(' '))
        
    def test_encode_uppercase(self):
        self.assertEqual('TqG', encoder('A'))
        
    def test_encode_multiple_characters(self):
        self.assertEqual('hXfVsWxMgZLrPcOeNbQdIjKlJkIpOhNmOmNLmkFjEhDgCcBbAa', encoder('Hello World'))
        
if __name__ == '__main__':
    unittest.main()