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
            newSquare = Square(0, 5)

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
        self.assertEqual(Square(4, 5).area(), 16)
        self.assertEqual(self.s2.area(), 16)
        self.assertEqual(self.s3.area(), 100)

    def test_str(self):
        """
        Testing __str__ method of the Square function
        """
        self.assertTrue(str(self.s2) == "[Square] (5) 6/0 - 4")
        self.assertEqual(str(self.s3), "[Square] (10) 6/2 - 10")

    def test_size_validation(self):
        """
        Testing the size attribute and making sure it is validate
        """
        self.assertTrue(self.s1.size == self.s1.width)
        self.s1.size = 15
        self.assertEqual(self.s1.size, 15)
        self.assertEqual(self.s1.width, 15)
        self.assertTrue(self.s1.width == self.s1.height)
        with self.assertRaises(TypeError) as e:
            self.s1.size = "4"

        self.assertEqual(str(e.exception), "width must be an integer")
        with self.assertRaises(ValueError) as m:
            self.s1.size = 0

        self.assertEqual(str(m.exception), "width must be > 0")

    def test_update(self):
        """
        Testing class Update
        """

        self.s2.update()
        self.assertEqual(str(self.s2), "[Square] (5) 6/0 - 4")
        self.s2.update(1)
        self.assertEqual(str(self.s2), "[Square] (1) 6/0 - 4")
        self.s2.update(1, 5)
        self.assertEqual(str(self.s2), "[Square] (1) 6/0 - 5")
        self.s2.update(1, 5, 10)
        self.assertEqual(str(self.s2), "[Square] (1) 10/0 - 5")
        self.s2.update(1, 5, 10, 9)
        self.assertEqual(str(self.s2), "[Square] (1) 10/9 - 5")
        self.s2.update(1, 5, 10, 9, 8)
        self.assertEqual(str(self.s2), "[Square] (1) 10/9 - 5")

    def test_update_with_kwargs(self):
        """
        Testing class update with keyword arguments
        """

        self.s2.update()
        self.assertEqual(str(self.s2), "[Square] (5) 6/0 - 4")
        self.s2.update(1, size=10)
        self.assertEqual(str(self.s2), "[Square] (1) 6/0 - 10")
        self.s2.update(1, 7, 2, y=3)
        self.assertEqual(str(self.s2), "[Square] (1) 2/3 - 7")
        self.s2.update(size=3, y=8, id=12, x=17)
        self.assertEqual(str(self.s2), "[Square] (12) 17/8 - 3")
        self.s2.update(2, 4, id=20, size=10)
        self.assertEqual(str(self.s2), "[Square] (2) 17/8 - 4")

    def test_to_dictionary_repr(self):
        """
        Testing the public method to_dictionary
        """

        self.assertIsInstance(self.s2.to_dictionary(), dict)
        self.assertEqual(self.s2.to_dictionary()["size"], 4)

        newSq = Square(9)
        self.s2.update(**newSq.to_dictionary())
        self.assertEqual(self.s2.size, 9)
        self.assertEqual(self.s2.id, newSq.id)
        self.assertTrue(self.s2.to_dictionary() == newSq.to_dictionary())
        output_dict = {
                "size": self.s2.size,
                "x": self.s2.x,
                "y": self.s2.y,
                "id": self.s2.id
            }
        self.assertEqual(self.s2.to_dictionary(), output_dict)
        self.assertTrue(newSq.to_dictionary() == output_dict)
