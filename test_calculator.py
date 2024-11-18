import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add01(self):
        self.assertEqual(self.calc.add(1, -1), 0)
    
    def test_add02(self):
        self.assertEqual(self.calc.add(1, -2), -1)

    def test_substract01(self):
        self.assertEqual(self.calc.subtract(1, -2), 3)

    def test_substract02(self):
        self.assertEqual(self.calc.subtract(-1, 2), -3)

    def test_multiply01(self):
        self.assertEqual(self.calc.multiply(1, -3), -3)

    def test_multiply02(self):
        self.assertEqual(self.calc.multiply(-1, -2), 2)

    def test_divide01(self):
        self.assertEqual(self.calc.divide(1, 1), 1)

    def test_divide02(self):
        self.assertEqual(self.calc.divide(-2, 2), -1)

    def test_modulo01(self):
        self.assertEqual(self.calc.modulo(1, 2), 1)

    def test_modulo02(self):
        self.assertEqual(self.calc.modulo(1, 1), 0)

if __name__ == '__main__':
    unittest.main()