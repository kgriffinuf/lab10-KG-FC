# https://github.com/kgriffinuf/lab10-KG-FC.git
# Partner 1: Kenneth Griffin
# Partner 2: Francisco Carmona

import unittest
from calculator import *
import math

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        # check if the results are equal to the expected
        expected = 8 * 7
        result = mul(8, 7)
        self.assertEqual(result, expected)

        # check if result is an integer
        self.assertIsInstance(result, int)

        # verify if the product(result) is greater than both variables a and b
        self.assertTrue(result >= 8 and result >= 7)

    def test_divide(self): # 3 assertions
        # ensure the result of div method is equal to the expected
        numerator = 10
        demoninator = 2
        expected = numerator / demoninator
        result = div(2, 10)
        # ensure demoninator is not equal to zero
        self.assertNotEqual(demoninator, 0, "demoninator cannot be zero")

        # ensure result is equal to expected
        self.assertEqual(result, expected)

        # ensure the result is a float
        self.assertIsInstance(result, float)

    #########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        a = 5
        b = 8
        self.assertNotEqual(a, 0, "a cannot be zero")
        self.assertNotEqual(b, 0, "a cannot be zero")
        # with self.assertRaises(ValueError):
        #     a != 0
        # with self.assertRaises(ValueError):
        #     b != 0
        expected = math.hypot(a, b)
        result = ((a ** 2) + (b ** 2)) ** (1/2)
        self.assertEqual(result, expected)


    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        expected = math.sqrt(self.a)
        result = math.sqrt(self.a)

        # a is greater than zero
        with self.assertRaises(ValueError):
            self.a < 0

        # result is a float
        self.assertIsInstance(result, float)

        # value error for assertRaises
        with self.assertRaises(ValueError):
            math.sqrt(self.a, self.b)

    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()