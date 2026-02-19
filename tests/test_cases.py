# Test Cases
import unittest
from basic_functions import factorial, find_max, count_vowels, is_palindrome,add, subtract, multiply,is_even


class TestAdvancedFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(0, 1), -1)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)

    def test_find_max(self):
        self.assertEqual(find_max([1, 5, 3]), 5)
        self.assertIsNone(find_max([]))

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))


if __name__ == "__main__":
    unittest.main()

