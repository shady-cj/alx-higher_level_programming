import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os
"""
This module contains a class that runs test on all
methods present in the Base class
"""


class BaseClassTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Sets up the TestCases
        """
        cls.base1 = Base()
        cls.base2 = Base()
        cls.base3 = Base(10)
        cls.base4 = Base()
        cls.base5 = Base()
        cls.base6 = Base(12)

    @classmethod
    def tearDownClass(cls):
        """
        Cleans out after all tests
        """
        os.remove("Rectangle.json")
        os.remove("Square.json")

    def test_BaseClassIds(self):
        """
        Testing Base class id values
        """
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.base3.id, 1)
        b = Base(2)
        self.assertTrue(b.id == self.base2.id)
        b2 = Base()
        self.assertEqual(b2.id, 5)
        self.assertEqual({2, 3}, Base({2, 3}).id)
        self.assertEqual("id", Base("id").id)

    def test_to_json_string_method(self):
        """
        Testing to_json_string() method with different
        edgecases
        """
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(3, 4, 7, 5, 3)
        rect3 = Rectangle(2, 7, id=2)

        new_list = [
                rect1.to_dictionary(),
                rect2.to_dictionary(),
                rect3.to_dictionary()
                ]
        self.assertIsInstance(new_list, list)
        self.assertEqual(len(new_list), 3)
        for d in new_list:
            self.assertIsInstance(d, dict)
        self.assertIsInstance(Base.to_json_string(new_list), str)
        self.assertIsNotNone(Base.to_json_string(None))
        self.assertIsInstance(Base.to_json_string(None), str)
        self.assertTrue(Base.to_json_string([]) == "[]")

    def test_save_to_file(self):
        """
        Testing save_to_file class method
        """
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(3, 4, 7, 5, 3)
        rect3 = Rectangle(2, 7, id=2)
        sq1 = Square(3)
        sq2 = Square(4, 3, 6, 7)
        sq3 = Square(3, id=5)
        list_objs = [
                rect1,
                rect2,
                rect3,
                sq1,
                sq2,
                sq3
            ]
        for obj in list_objs:
            self.assertIsInstance(obj, Base)
        Rectangle.save_to_file(list_objs[:3])
        Square.save_to_file(list_objs[3:])
        import os
        self.assertTrue(os.path.isfile("Rectangle.json"))
        self.assertTrue(os.path.isfile("Square.json"))
        r_content = None
        s_content = None
        with open("Rectangle.json") as f:
            r_content = f.read()
            self.assertIsInstance(r_content, str)
            self.assertIsInstance(eval(r_content), list)
            self.assertEqual(len(eval(r_content)), 3)
            for n in eval(r_content):
                self.assertIsInstance(n, dict)
        with open("Square.json") as sf:
            s_content = sf.read()
            self.assertIsInstance(s_content, str)
            self.assertIsInstance(eval(s_content), list)

        output = [
                rect1.to_dictionary(),
                rect2.to_dictionary(),
                rect3.to_dictionary(),
                sq1.to_dictionary(),
                sq2.to_dictionary(),
                sq3.to_dictionary()
            ]
        self.assertEqual(eval(r_content), output[:3])
        self.assertEqual(eval(s_content), output[3:])

    def test_from_json_string(self):
        """
        Testing from_json_string() static method with different
        edge scenarios
        """
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(3, 4, 7, 5, 3)
        rect3 = Rectangle(2, 7, id=2)
        sq1 = Square(3)
        sq2 = Square(4, 3, 6, 7)
        sq3 = Square(3, id=5)
        list_of_dicts = [
                rect1.to_dictionary(),
                rect2.to_dictionary(),
                rect3.to_dictionary(),
                sq1.to_dictionary(),
                sq2.to_dictionary(),
                sq3.to_dictionary()
            ]

        import json
        json_string = Base.to_json_string(list_of_dicts)
        return_v = Base.from_json_string(json_string)
        self.assertEqual(return_v, list_of_dicts)
        self.assertIsInstance(return_v, list)
        self.assertIsNotNone(Base.from_json_string(None))
        self.assertIsInstance(Base.from_json_string(""), list)

    def test_create_method(self):
        """
        Testing the create() classmethod with edge cases
        """

        rect = Rectangle(2, 3)
        sq = Square(3)

        new_rect = Rectangle.create(**rect.to_dictionary())
        new_sq = Square.create(**sq.to_dictionary())
        self.assertIsInstance(new_rect, rect.__class__)
        self.assertIsInstance(new_sq, sq.__class__)
        self.assertEqual(new_sq.to_dictionary(), sq.to_dictionary())
        self.assertEqual(new_rect.to_dictionary(), rect.to_dictionary())
        self.assertFalse(new_rect == rect)
        self.assertFalse(new_sq == sq)

        wrong_rect = {
                "width": 3,
                "height": 0,
                "id": 2,
                "x": 4,
                "y": 2
                }
        self.assertRaises(TypeError, Base.create, **wrong_rect)

    def test_load_from_file(self):
        """
        Testing load_from_file() from the Base class
        """
        self.assertEqual(Square.load_from_file(), [])
        self.assertEqual(Rectangle.load_from_file(), [])
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(3, 4, 7, 5, 3)
        rect3 = Rectangle(2, 7, id=2)
        sq1 = Square(3)
        sq2 = Square(4, 3, 6, 7)
        sq3 = Square(3, id=5)
        list_obj_sq = [
                sq1,
                sq2,
                sq3
            ]
        list_obj_rect = [
                rect1,
                rect2,
                rect3
            ]
        Rectangle.save_to_file(list_obj_rect)
        Square.save_to_file(list_obj_sq)
        s = Square.load_from_file()
        r = Rectangle.load_from_file()
        self.assertNotEqual(s, list_obj_sq)
        self.assertNotEqual(r, list_obj_rect)
        self.assertIsInstance(s, list)
        self.assertIsInstance(r, list)
        for obj_s in s:
            self.assertIsInstance(obj_s, Square)
        for obj_r in r:
            self.assertIsInstance(obj_r, Rectangle)
        """
        Showing save_to_file() will overwrite
        existing files
        """
        list_obj_rect = [
                rect2
            ]
        list_obj_sq = [
                sq2
            ]
        Rectangle.save_to_file(list_obj_rect)
        Square.save_to_file(list_obj_sq)
        new_s = Square.load_from_file()
        new_r = Rectangle.load_from_file()

        self.assertNotEqual(new_s, list_obj_sq)
        self.assertNotEqual(new_r, list_obj_rect)
        self.assertNotEqual(new_s, s)
        self.assertEqual(len(new_s), 1)
        self.assertIsInstance(new_s, list)


if __name__ == "__main__":
    unittest.main()
