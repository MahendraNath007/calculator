# test_calculator.py

import unittest
from calculator_logic import CalculatorLogic


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = CalculatorLogic()

    # Positive cases
    def test_add_positive(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    # Negative cases
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-5, 3), -2)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-4, -2), 8)

    # Zero cases
    def test_add_zero(self):
        self.assertEqual(self.calc.add(0, 7), 7)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(9, 0), 9)

    # Division
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)


if __name__ == "__main__":
    unittest.main()