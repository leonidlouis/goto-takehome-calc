import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2), 2.0)
        self.assertEqual(self.calc.add(-5), -3.0)
        self.assertEqual(self.calc.add(3), 0.0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2), -2.0)
        self.assertEqual(self.calc.subtract(-5), 3.0)
        self.assertEqual(self.calc.subtract(3), 0.0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2), 0.0)
        self.calc.add(3)
        self.assertEqual(self.calc.multiply(2), 6.0)
        self.assertEqual(self.calc.multiply(0), 0.0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(0), "Division by zero is not allowed!")
        self.calc.add(4)
        self.assertEqual(self.calc.divide(2), 2.0)
        self.assertEqual(self.calc.divide(-1), -2.0)

    def test_neg(self):
        self.assertEqual(self.calc.neg(), 0.0)
        self.calc.add(4)
        self.assertEqual(self.calc.neg(), -4.0)
        self.assertEqual(self.calc.neg(), 4.0)

    def test_abs(self):
        self.assertEqual(self.calc.abs(), 0.0)
        self.calc.add(-4)
        self.assertEqual(self.calc.abs(), 4.0)

    def test_sqr(self):
        self.calc.add(2)
        self.assertEqual(self.calc.sqr(), 4.0)
        self.calc.add(-2)
        self.assertEqual(self.calc.sqr(), 4.0)

    def test_sqrt(self):
        self.calc.add(4)
        self.assertEqual(self.calc.sqrt(), 2.0)

    def test_cube(self):
        self.calc.add(2)
        self.assertEqual(self.calc.cube(), 8.0)

    def test_cubert(self):
        self.calc.add(8)
        self.assertEqual(self.calc.cubert(), 2.0)

    def test_cancel(self):
        self.calc.add(5)
        self.assertEqual(self.calc.cancel(), 0.0)
        self.assertEqual(self.calc.total, 0.0)
        self.assertEqual(len(self.calc.history), 0)

    def test_repeat(self):
        self.calc.add(1)
        self.calc.subtract(1)
        self.calc.multiply(5)
        self.assertEqual(self.calc.repeat(2), -5.0)

    def test_invalid_command(self):
        result = self.calc.execute("invalid_command 5")
        self.assertEqual(result, "Unrecognized command: invalid_command")

    def test_history(self):
        self.calc.add(1)
        self.calc.subtract(1)
        self.assertEqual(len(self.calc.history), 2)
        self.assertEqual(self.calc.history[-1], ("subtract", 1))

    def test_mixed_sequence(self):
        self.assertEqual(self.calc.add(2), 2.0)
        self.assertEqual(self.calc.neg(), -2.0)
        self.assertEqual(self.calc.sqr(), 4.0)
        self.assertEqual(self.calc.multiply(2), 8.0)
        self.assertEqual(self.calc.repeat(2), 128.0)
        self.assertEqual(self.calc.divide(2), 64.0)
        self.assertEqual(self.calc.sqrt(), 8.0)
        self.assertEqual(self.calc.cube(), 512.0)
        self.assertEqual(self.calc.cubert(), 8.0)
        self.assertEqual(self.calc.subtract(10), -2.0)
        self.assertEqual(self.calc.abs(), 2.0)
        self.assertEqual(self.calc.cancel(), 0.0)

    def test_multiply_without_value(self):
        response = self.calc.execute("multiply")
        expected_message = "'multiply' command requires a numeric value."
        self.assertEqual(response, expected_message)

    def test_multiply_with_non_numeric_value(self):
        response = self.calc.execute("multiply asd")
        expected_message = "You must input numbers for the 'multiply' operation."
        self.assertEqual(response, expected_message)

    def test_add_without_value(self):
        response = self.calc.execute("add")
        expected_message = "'add' command requires a numeric value."
        self.assertEqual(response, expected_message)

    def test_add_with_non_numeric_value(self):
        response = self.calc.execute("add xyz")
        expected_message = "You must input numbers for the 'add' operation."
        self.assertEqual(response, expected_message)

    def test_subtract_without_value(self):
        response = self.calc.execute("subtract")
        expected_message = "'subtract' command requires a numeric value."
        self.assertEqual(response, expected_message)

    def test_subtract_with_non_numeric_value(self):
        response = self.calc.execute("subtract qwe")
        expected_message = "You must input numbers for the 'subtract' operation."
        self.assertEqual(response, expected_message)

    def test_divide_without_value(self):
        response = self.calc.execute("divide")
        expected_message = "'divide' command requires a numeric value."
        self.assertEqual(response, expected_message)

    def test_divide_with_non_numeric_value(self):
        response = self.calc.execute("divide rty")
        expected_message = "You must input numbers for the 'divide' operation."
        self.assertEqual(response, expected_message)

    def test_neg_with_value(self):
        response = self.calc.execute("neg 12")
        expected_message = "'neg' command doesn't accept a value."
        self.assertEqual(response, expected_message)

    def test_abs_with_value(self):
        response = self.calc.execute("abs 123")
        expected_message = "'abs' command doesn't accept a value."
        self.assertEqual(response, expected_message)

    def test_sqr_with_value(self):
        response = self.calc.execute("sqr 10")
        expected_message = "'sqr' command doesn't accept a value."
        self.assertEqual(response, expected_message)

    def test_sqrt_with_value(self):
        response = self.calc.execute("sqrt 4")
        expected_message = "'sqrt' command doesn't accept a value."
        self.assertEqual(response, expected_message)

    def test_cube_with_value(self):
        response = self.calc.execute("cube 3")
        expected_message = "'cube' command doesn't accept a value."
        self.assertEqual(response, expected_message)

    def test_cubert_with_value(self):
        response = self.calc.execute("cubert 8")
        expected_message = "'cubert' command doesn't accept a value."
        self.assertEqual(response, expected_message)

    def test_cancel_with_value(self):
        response = self.calc.execute("cancel 10")
        expected_message = "'cancel' command doesn't accept a value."
        self.assertEqual(response, expected_message)
        
if __name__ == "__main__":
    unittest.main()