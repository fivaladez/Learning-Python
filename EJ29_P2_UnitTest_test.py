# EJ29_P2    UnitTest 2
from EJ28_P2_UnitTest import circle_area
import unittest
from math import pi

# To RUN this code use:
#   python -m unittest file_name


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test ares when raduis >= 0
        # assertAlmostEqual( function to test, expected result )
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        # Make sure value errors are raised when necessary
        # assertRaises( exception class to raise, function to test, arguments )
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
# help(unittest.TestCase.assertSetEqual)
