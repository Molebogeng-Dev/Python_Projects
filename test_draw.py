import unittest
from draw import draw_square, draw_triangle, draw_hollow_rectangle

class TestDrawShapes(unittest.TestCase):
    def test_draw_square(self):
        expected = "****\n****\n****\n****"
        self.assertEqual(draw_square(4), expected)

    def test_draw_triangle(self):
        expected = "*\n**\n***\n****"
        self.assertEqual(draw_triangle(4), expected)

    def test_draw_hollow_rectangle(self):
        expected = "*****\n*   *\n*   *\n*****"
        self.assertEqual(draw_hollow_rectangle(5, 4), expected)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            draw_square(0)
        with self.assertRaises(ValueError):
            draw_triangle(-3)
        with self.assertRaises(ValueError):
            draw_hollow_rectangle(4, 0)

if __name__ == '__main__':
    unittest.main()
