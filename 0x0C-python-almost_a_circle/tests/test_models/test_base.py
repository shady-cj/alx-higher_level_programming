import unittest
from models.base import Base

class BaseClassTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.base1 = Base()
        self.base2 = Base()
        self.base3 = Base(10)
        self.base4 = Base()
        self.base5 = Base()
        self.base6 = Base(12)

    def test_BaseClassIds(self):
        """
        Testing Base class id values
        """
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.base3.id, 10)
        b = Base(2)
        self.assertTrue(b.id == self.base2.id)
        b2 = Base()
        self.assertEqual(b2.id, 5)

if __name__ == "__main__":
    unittest.main()
