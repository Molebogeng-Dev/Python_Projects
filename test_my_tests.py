import unittest
from fundamentals import check_number

class MyTestCases(unittest.TestCase):
    def test_check_number_odd_number(self):
        self.assertEqual(check_number(1,9), (1,3,5,7,9))

    def test_check_number_even_range_2_to_5(self):
        self.assertEqual(check_number(2, 5), ("Not Weird"))

    def test_check_number_even_range_6_to_20(self):
        self.assertEqual(check_number(6, 20), ("Weird"))
        self.assertEqual(check_number(6, 20), ("Not Weird"))

    def test_check_number_negative_even_number(self):
        self.assertEqual(check_number(-2, -20), (-2,-4,-6,-8,-10,-12,-14,-16,-18,-20))

    def test_check_number_negative_odd_number(self):
        self.assertEqual(check_number(-1, -19), (-1,-3,-5,-7,-9,-11,-13,-15,-17,-19))

    def test_check_number_neutral(self):
        self.assertEqual(check_number(-1,0,1),(-1,1))


if __name__=='__main__':
    unittest.main()
