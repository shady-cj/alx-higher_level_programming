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
