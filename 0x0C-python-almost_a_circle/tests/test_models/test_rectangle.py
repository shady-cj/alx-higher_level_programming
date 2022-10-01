import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTestCases(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(3, 4)
        self.r2 = Rectangle(4, 6, id=5)
        self.b = Base()
        self.r3 = Rectangle(10, 6, 2, 5)

    def test_rectangleArgs(self):
        """
        Testing rectangle arguments
        """
        self.assertEqual(self.r1.width, 3)
        self.assertEqual(self.r1.x, self.r1.y)
        with self.assertRaises(AttributeError):
            self.assertEqual(self.r1.__width, 3)
        self.assertEqual(self.r2.id, 5)
        self.assertFalse(self.r3.id == 2)

    def test_typeValidation(self):
        """
        Testing the width, height, x and y type validation
        """
        with self.assertRaises(TypeError) as e:
            newRect = Rectangle("3", 7)
        with self.assertRaises(TypeError):
            newRect = Rectangle(5, (4,))
        self.assertTrue(str(e.exception) == "width must be an integer")
        self.assertRaises(TypeError, Rectangle, 2, 4, {4}, {4})
    
    def test_valueValidation(self):
        """
        Testing the value validation of the arguments
        """

        with self.assertRaises(ValueError):
            newRect = Rectangle(0,5)

        with self.assertRaises(ValueError) as e:
            newRect = Rectangle(4, -6)
        self.assertEqual(str(e.exception), "height must be > 0")
        self.assertRaises(ValueError, Rectangle, 4, 6, -3)

    def test_noArgs(self):
        """Testing for no arguments to Rectangle class"""
        self.assertRaises(TypeError, Rectangle)

    def test_area(self):
        """
        Testing the area of the rectangle
        """
        self.assertEqual(self.r1.area(), 12)
        self.assertEqual(Rectangle(4,4).area(), 16)
        self.assertEqual(self.r2.area(), 24)
        self.assertEqual(self.r3.area(), 60)

    def test_str(self):
        """
        Testing __str__ method of the Rectangle function
        """
        self.assertTrue(str(self.r2) == "[Rectangle] (5) 0/0 - 4/6")
        self.r3.id = 8
        self.assertEqual(str(self.r3), "[Rectangle] (8) 2/5 - 10/6")
