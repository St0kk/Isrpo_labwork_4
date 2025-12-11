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

    def test_positive_int_radius_area(self):
        res = circle.area(2)
        self.assertEqual(res, 4 * math.pi)

    def test_positive_float_radius_area(self):
        res = circle.area(2.4)
        self.assertEqual(res, 2.4 * 2.4 * math.pi)
    
    def test_negative_radius_area(self):
        res = circle.area(-2)
        self.assertEqual(res, 4 * math.pi) 
    
    def test_negative_float_radius_area(self):
        res = circle.area(-2.4)
        self.assertEqual(res, 2.4 * 2.4 * math.pi) 

    def test_zero_radius_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_int_radius_perimeter(self):
        res = circle.perimeter(2)
        self.assertEqual(res, 2 * 2 * math.pi)

    def test_positive_float_radius_perimeter(self):
        res = circle.perimeter(2.4)
        self.assertEqual(res, 2 * 2.4 * math.pi)

    def test_negative_int_radius_perimeter(self):
        res = circle.perimeter(-2)
        self.assertEqual(res, 2 * (-2) * math.pi)

    def test_negative_float_radius_perimeter(self):
        res = circle.perimeter(-2.4)
        self.assertEqual(res, 2 * (-2.4) * math.pi)


class RectangleTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = rectangle.area(0, 5)
        self.assertEqual(res, 0)
        res = rectangle.area(5, 0)
        self.assertEqual(res, 0)

    def test_positive_int_sides_area(self):
        res = rectangle.area(2, 4)
        self.assertEqual(res, 8)
    
    def test_positive_float_sides_area(self):
        res = rectangle.area(2.4, 4.2)
        self.assertEqual(res, 2.4 * 4.2)
    
    def test_positive_float_and_int_sides_area(self):
        res = rectangle.area(2.4, 4)
        self.assertEqual(res, 2.4 * 4)
        res = rectangle.area(2, 4.2)
        self.assertEqual(res, 2 * 4.2)
    
    def test_negative_sides_area(self):
        res = rectangle.area(-2, 4)
        self.assertEqual(res, -8) 
    
    def test_both_negative_sides_area(self):
        res = rectangle.area(-2, -4)
        self.assertEqual(res, 8)  
    
    def test_negative_float_sides_area(self):
        res = rectangle.area(-2.4, 4.2)
        self.assertEqual(res, -2.4 * 4.2)

    def test_zero_side_perimeter(self):
        res = rectangle.perimeter(0, 5)
        self.assertEqual(res, 10)
        res = rectangle.perimeter(5, 0)
        self.assertEqual(res, 10)

    def test_positive_int_sides_perimeter(self):
        res = rectangle.perimeter(2, 4)
        self.assertEqual(res, 12)
    
    def test_positive_int_and_float_sides_perimeter(self):
        res = rectangle.perimeter(2.4, 4)
        self.assertEqual(res, 2 * 2.4 + 2 * 4)
        res = rectangle.perimeter(2, 4.2)
        self.assertEqual(res, 2 * 2 + 2 * 4.2)
    
    def test_negative_sides_perimeter(self):
        res = rectangle.perimeter(-2, 4)
        self.assertEqual(res, 2 * (-2) + 2 * 4)
    
    def test_both_negative_sides_perimeter(self):
        res = rectangle.perimeter(-2, -4)
        self.assertEqual(res, 2 * (-2) + 2 * (-4))
    
    def test_negative_float_sides_perimeter(self):
        res = rectangle.perimeter(-2.4, 4.2)
        self.assertEqual(res, 2 * (-2.4) + 2 * 4.2)


class SquareTestCase(unittest.TestCase):
    def test_zero_side_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_positive_int_side_area(self):
        res = square.area(3)
        self.assertEqual(res, 9)
    
    def test_positive_float_side_area(self):
        res = square.area(3.2)
        self.assertEqual(res, 3.2 * 3.2)
    
    def test_negative_side_area(self):
        res = square.area(-3)
        self.assertEqual(res, 9) 
    
    def test_negative_float_side_area(self):
        res = square.area(-3.2)
        self.assertEqual(res, 3.2 * 3.2) 

    def test_zero_side_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_side_int_perimeter(self):
        res = square.perimeter(3)
        self.assertEqual(res, 12)
    
    def test_positive_side_float_perimeter(self):
        res = square.perimeter(3.2)
        self.assertEqual(res, 3.2 * 4)
    
    def test_negative_side_perimeter(self):
        res = square.perimeter(-3)
        self.assertEqual(res, -12)  
    
    def test_negative_float_side_perimeter(self):
        res = square.perimeter(-3.2)
        self.assertEqual(res, -3.2 * 4)


class TriangleTestCase(unittest.TestCase):
    def test_zero_base_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_zero_height_area(self):
        res = triangle.area(4, 0)
        self.assertEqual(res, 0)

    def test_positive_int_values_area(self):
        res = triangle.area(4, 6)
        self.assertEqual(res, 12)
    
    def test_positive_float_values_area(self):
        res = triangle.area(4.6, 6.4)
        self.assertEqual(res, (4.6 * 6.4) / 2)
    
    def test_positive_int_and_float_values_area(self):
        res = triangle.area(4.6, 6)
        self.assertEqual(res, (4.6 * 6) / 2)
        res = triangle.area(4, 6.4)
        self.assertEqual(res, (4 * 6.4) / 2)
    
    def test_negative_base_area(self):
        res = triangle.area(-4, 6)
        self.assertEqual(res, -12) 
    
    def test_negative_height_area(self):
        res = triangle.area(4, -6)
        self.assertEqual(res, -12) 
    
    def test_both_negative_values_area(self):
        res = triangle.area(-4, -6)
        self.assertEqual(res, 12) 
    
    def test_negative_float_values_area(self):
        res = triangle.area(-4.6, 6.4)
        self.assertEqual(res, (-4.6 * 6.4) / 2)

    def test_zero_sides_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_positive_int_sides_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_positive_float_sides_perimeter(self):
        res = triangle.perimeter(3.4, 4.5, 5.3)
        self.assertEqual(res, 3.4 + 4.5 + 5.3)
    
    def test_positive_int_and_float_sides_perimeter(self):
        res = triangle.perimeter(3, 4, 5.3)
        self.assertEqual(res, 3 + 4 + 5.3)
        res = triangle.perimeter(3.3, 4, 5.3)
        self.assertEqual(res, 3.3 + 4 + 5.3)
        res = triangle.perimeter(3, 4.2, 5)
        self.assertEqual(res, 3 + 4.2 + 5)
    
    def test_negative_sides_perimeter(self):
        res = triangle.perimeter(-3, 4, 5)
        self.assertEqual(res, -3 + 4 + 5)
    
    def test_multiple_negative_sides_perimeter(self):
        res = triangle.perimeter(-3, -4, 5)
        self.assertEqual(res, -3 + (-4) + 5)
    
    def test_all_negative_sides_perimeter(self):
        res = triangle.perimeter(-3, -4, -5)
        self.assertEqual(res, -3 + (-4) + (-5))
    
    def test_negative_float_sides_perimeter(self):
        res = triangle.perimeter(-3.4, 4.5, 5.3)
        self.assertEqual(res, -3.4 + 4.5 + 5.3)