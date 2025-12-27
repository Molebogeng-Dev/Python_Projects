import unittest
from basics import add_numbers, is_even, reverse_string, factorial

class TestBasics(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)

    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))

    def test_reverse_string(self):
        self.assertEqual(reverse_string("python"), "nohtyp")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string(""), "")

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        with self.assertRaises(ValueError):
            factorial(-3)

if __name__ == '__main__':
    unittest.main()
