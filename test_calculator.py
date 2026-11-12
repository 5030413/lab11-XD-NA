# https://github.com/5030413/lab11-XD-NA
# Partner 1: Xinlin Du
# Partner 2: Natasha Antoniuk

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2 (Natasha)
    def test_add(self): # 3 assertions
        self.assertEqual(add(-7, -7), -14)
        self.assertEqual(add(-7,7),0)
        self.assertEqual(add(7,7),14)
    # ##########################

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(-7,7),-14)
        self.assertEqual(subtract(7,-7),14)
        self.assertEqual(subtract(7,7),0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1, 0), 0)
        self.assertEqual(mul(2, -3), -6)
        self.assertEqual(mul(-9, -7), 63)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 6), 2)
        self.assertEqual(div(-3, 6), -2)
        with self.assertRaises(ZeroDivisionError):
            div(0, 3)
    # ##########################

    ######## Partner 2 (Natasha)
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10,100),2)
        self.assertEqual(logarithm(2,4),2)
        self.assertNotEqual(logarithm(3,4),2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-1,5)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-5, 12), 13)
        self.assertEqual(hypotenuse(0, 5), 5)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-1)
        with self.assertRaises(ValueError):
           square_root(-100)
        self.assertEqual(square_root(16), 4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()