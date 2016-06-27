import unittest
from third import count_letter_in_string

class TestCountLetterInString(unittest.TestCase):
    def test_input_is_string(self):
        self.assertEqual(count_letter_in_string('apple', 'e'), 1)

    def test_empty_input(self):
        self.assertEqual(count_letter_in_string('', 'e'), 0)

    def test_input_is_number(self):
        self.assertEqual(count_letter_in_string(897, 'a'), 0)

    def test_input_is_list(self):
        self.assertEqual(count_letter_in_string(['apple', 'blueberry', 'banana'], 'a'), 0)
        
    def test_input_is_boolean(self):
        self.assertEqual(count_letter_in_string(True, 'r'), 0)

    def test_letter_more_than_one_char(self):
        self.assertEqual(count_letter_in_string('apple', 'pl'), 0)

    def test_uppercase_letters_in_string(self):
        self.assertNotEqual(count_letter_in_string('apPLe', 'p'), 2)

    def test_given_letter_is_not_letter(self):
        self.assertEqual(count_letter_in_string('apple', 8), 0)

if __name__ == '__main__':
    unittest.main()
