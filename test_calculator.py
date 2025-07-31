# https://github.com/kgriffinuf/lab10-KG-FC.git
# Partner 1: Kenneth Griffin
# Partner 2: Francisco Carmona

import unittest
from calculator import *
import math

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        # test the add function in calculator.py
        # assertion 1
        a, b = 1, 2
        expected = 3
        self.assertEqual(add(a, b), expected)

        # assertion 2
        a, b = 500, 650
        expected = 1150
        self.assertEqual(add(a, b), expected)

        # assertion 3
        a, b = 800, 1200
        expected = 12000
        self.assertEqual(add(a, b), expected)

    def test_subtract(self): # 3 assertions
        # Test sub function in calculator.py
        # assertion 1
        a, b = 1, 2
        expected = 1
        self.assertEqual(sub(a, b), expected)

        # assertion 2
        a, b = 650, 500
        expected = 150
        self.assertEqual(sub(a, b), expected)

        # assertion 3
        a, b = 800, 1200
        expected = -400
        self.assertEqual(sub(a, b), expected)
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
        # ensure a is not equal to zero
        assert self.a != 0, "Zero Division Error"

        # ensure the result of div method is equal to the expected
        expected = self.b / self.a
        result = self.div
        self.assertEqual(result, expected)

        # ensure the result is a float
        self.assertIsInstance(result, float)
    #########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self): # 3 assertions
        # assertion 1
        a, b = 2, 8
        expected = 3
        self.assertEqual(log(a, b), expected)

        # assertion 2
        a, b = 2, 16
        expected = 4
        self.assertEqual(log(a, b), expected)

        # assertion 3
        a, b = 10, 1000
        expected = 3
        self.assertEqual(log(a, b), expected)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 10)
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        with self.assertRaises(ValueError):
            self.a != 0
        with self.assertRaises(ValueError):
            self.b != 0
        expected = math.hypot(self.a, self.b)
        result = self.hypotenuse
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