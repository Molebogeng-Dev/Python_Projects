import unittest
import basic_syntax

class TestBasicSyntax(unittest.TestCase):

    def test_assign_variables(self):
        x, y, z, a, b = basic_syntax.assign_variables()
        self.assertEqual(x, 10)
        self.assertEqual(y, 20.5)
        self.assertEqual(z, 'Hello, World!')
        self.assertEqual(a, True)
        self.assertEqual(b, False)

    def test_get_variable_types(self):
        type_x, type_y, type_z, type_a, type_b = basic_syntax.get_variable_types()
        self.assertEqual(type_x, 'int')
        self.assertEqual(type_y, 'float')
        self.assertEqual(type_z, 'str')
        self.assertEqual(type_a, 'bool')
        self.assertEqual(type_b, 'bool')

    def test_arithmetic_operations(self):
        sum_result, difference_result, product_result, division_result, modulus_result = basic_syntax.arithmetic_operations()
        self.assertEqual(sum_result, 10 + 20.5)
        self.assertEqual(difference_result, 10 - 20.5)
        self.assertEqual(product_result, 10 * 20.5)
        self.assertEqual(division_result, 10 / 20.5)
        self.assertEqual(modulus_result, 10 % 20.5)

    def test_get_numbers(self):
        numbers = basic_syntax.get_numbers()
        self.assertEqual(numbers, [0, 1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
