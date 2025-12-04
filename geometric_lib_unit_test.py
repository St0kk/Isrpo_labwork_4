import unittest
import math
import circle
import square
import rectangle
import triangle


class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_positive_radius_area(self):
        res = circle.area(2)
        self.assertEqual(res, 4 * math.pi)
    
    def test_zero_radius_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_radius_perimeter(self):
        res = circle.perimeter(2)
        self.assertEqual(res, 2 * 2 * math.pi)


class RectangleTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = rectangle.area(0, 5)
        self.assertEqual(res, 0)
        res = rectangle.area(5, 0)
        self.assertEqual(res, 0)

    def test_positive_sides_area(self):
        res = rectangle.area(2, 4)
        self.assertEqual(res, 8)
    
    def test_zero_side_perimeter(self):
        res = rectangle.perimeter(0, 5)
        self.assertEqual(res, 10)

    def test_positive_sides_perimeter(self):
        res = rectangle.perimeter(2, 4)
        self.assertEqual(res, 12)


class SquareTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_positive_side_area(self):
        res = square.area(3)
        self.assertEqual(res, 9)
    
    def test_zero_side_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_side_perimeter(self):
        res = square.perimeter(3)
        self.assertEqual(res, 12)


class TriangleTestCase(unittest.TestCase):
    def test_zero_base_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_zero_height_area(self):
        res = triangle.area(4, 0)
        self.assertEqual(res, 0)

    def test_positive_values_area(self):
        res = triangle.area(4, 6)
        self.assertEqual(res, 12)
    
    def test_zero_sides_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_positive_sides_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
