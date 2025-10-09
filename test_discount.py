import unittest
from src.main import calculate_discount

class TestDiscount(unittest.TestCase):
    def test_basic_discount(self):
        self.assertEqual(calculate_discount(100, 10), 90.0)
        self.assertEqual(calculate_discount(200, 25), 150.0)

    def test_cap_at_90(self):
        self.assertEqual(calculate_discount(100, 95), 10.0)

    def test_negative_inputs(self):
        with self.assertRaises(ValueError):
            calculate_discount(-100, 10)
        with self.assertRaises(ValueError):
            calculate_discount(100, -10)

if __name__ == '__main__':
    unittest.main()
