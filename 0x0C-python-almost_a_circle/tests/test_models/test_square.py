import unittest
from models.square import Square


class SquareTestCases(unittest.TestCase):
    def setUp(self):
        self.s1 = Square(3)
        self.s2 = Square(4, 6, id=5)
        self.s3 = Square(10, 6, 2, 10)

    def test_squareArgs(self):
        """
        Testing square arguments
        """
        self.assertEqual(self.s1.width, self.s1.height)
        self.assertEqual(self.s1.x, self.s1.y)
        with self.assertRaises(AttributeError):
            self.assertEqual(self.s1.__width, 3)
        self.assertEqual(self.s2.id, 5)
        self.assertTrue(self.s3.id == 10)

    def test_typeValidation(self):
        """
        Testing the width, height, x and y type validation
        """
        with self.assertRaises(TypeError) as m:
            newSquare = Square("3")
        self.assertEqual(str(m.exception), "width must be an integer")
        with self.assertRaises(TypeError) as e:
            newSquare = Square(18, (4,), 7)
        self.assertTrue(str(e.exception) == "x must be an integer")
        self.assertRaises(TypeError, Square, 2, {4}, {4})

    def test_valueValidation(self):
        """
        Testing the value validation of the arguments
        """

        with self.assertRaises(ValueError):
            newSquare = Square(0,5)

        with self.assertRaises(ValueError) as e:
            newSquare = Square(4, -6)
        self.assertEqual(str(e.exception), "x must be >= 0")
        self.assertRaises(ValueError, Square, 4, 6, -3)

    def test_noArgs(self):
        """Testing for no arguments to Square class"""
        self.assertRaises(TypeError, Square)

    def test_area(self):
        """
        Testing the area of the square
        """
        self.assertEqual(self.s1.area(), 9)
        self.assertEqual(Square(4,5).area(), 16)
        self.assertEqual(self.s2.area(), 16)
        self.assertEqual(self.s3.area(), 100)

    def test_str(self):
        """
        Testing __str__ method of the Square function
        """
        self.assertTrue(str(self.s2) == "[Square] (5) 6/0 - 4")
        self.assertEqual(str(self.s3), "[Square] (10) 6/2 - 10")

    """
    def test_update(self):
        ""
        Testing class Update
        ""

        self.s2.update()
        self.assertEqual(str(self.r2), "[Rectangle] (5) 0/0 - 4/6")
        self.s2.update(1)
        self.assertEqual(str(self.r2), "[Rectangle] (1) 0/0 - 4/6")
        self.r2.update(1, 5)
        self.assertEqual(str(self.r2), "[Rectangle] (1) 0/0 - 5/6")
        self.r2.update(1,5,10)
        self.assertEqual(str(self.r2), "[Rectangle] (1) 0/0 - 5/10")
        self.r2.update(1,5,10,9)
        self.assertEqual(str(self.r2), "[Rectangle] (1) 9/0 - 5/10")
        self.r2.update(1,5,10,9,8)
        self.assertEqual(str(self.r2), "[Rectangle] (1) 9/8 - 5/10")

    def test_update_with_kwargs(self):
        ""
        Testing class update with keyword arguments
        ""

        self.r2.update()
        self.assertEqual(str(self.r2), "[Rectangle] (5) 0/0 - 4/6")
        self.r2.update(1, height=10)
        self.assertEqual(str(self.r2), "[Rectangle] (1) 0/0 - 4/10")
        self.r2.update(1, 7, 2, y=3)
        self.assertEqual(str(self.r2), "[Rectangle] (1) 0/3 - 7/2")
        self.r2.update(width=3, y=8, height=2, id=12, x=17)
        self.assertEqual(str(self.r2), "[Rectangle] (12) 17/8 - 3/2")
        self.r2.update(2,4,id=20, width=10)
        self.assertEqual(str(self.r2), "[Rectangle] (2) 17/8 - 4/2")
    """
