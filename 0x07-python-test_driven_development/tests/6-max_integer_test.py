import unittest
max_integer = __import__('6-max_integer').max_integer

"""
This module creates testcases to test the 6-max_integer.py module
"""


class TestMaxInteger(unittest.TestCase):
    """
    The class inherits from the unittest.TestCase class
    """

    def test_empty_list(self):
        """Test for empty lists and it's expected to return None"""
        self.assertIsNone(max_integer([]))

    def test_max_int(self):
        """
        Test for the maximum integer present in a list and expects to
        return the correct result
        """
        self.assertEqual(max_integer([1, 4, 2, 6]), 6)
        self.assertIsNotNone(max_integer([3, 1, 2]))
        self.assertEqual(max_integer([0, -3, -72]), 0)

    def test_multiple_max_int(self):
        """
        Test for multiple maximum number
        """
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([5, 2, 3, 5]), 5)

    def test_one_element_in_the_list(self):
        """
        Test for one element in the list
        """
        self.assertEqual(max_integer([8]), 8)
        self.assertIsNotNone(max_integer([0]))
    
    def test_for_maxelement_in_the_middle(self):
        """
        Test when max element is in the middle
        """

        self.assertEqual(max_integer([3,2,6,1,9,5,7,1,4]), 9)
        self.assertEqual(max_integer([2,4,4,1]), 4)
