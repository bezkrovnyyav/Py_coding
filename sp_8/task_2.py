"""
You have function divide:

def divide(num_1, num_2):
    if num_2 > 0:
        return float(num_1) / num_2

Please, write the code with unit tests for the function "divide":
minimum 3 tests
must chek all flows
all test must be pass
no failures
no skip
"""
import unittest


def divide(num_1, num_2):
    if num_2 > 0:
        return float(num_1) / num_2
        
        
class DivideTest(unittest.TestCase):
    def test_first_divide(self):
        expected = 2.75
        actual = divide(5.5, 2)
        self.assertEqual(expected, actual)

    def test_second_divide(self):
        expected = 0.333
        actual = divide(1, 3)
        self.assertAlmostEqual(expected, actual, 3)
    
    def test_division_via_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 3, 0)