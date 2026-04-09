import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self): self.calc = Calculator() # Fresh instance per test

    def test_add(self): 
        result = self.calc.add(10, 5)
        print(f"Add Result: {result}")
        self.assertEqual(result, 15)

    def test_subtract(self): 
        result = self.calc.subtract(12, 6)
        print(f"Subtract Result: {result}")
        self.assertEqual(result, 6)

    def test_multiply(self): 
        result = self.calc.multiply(3, 4)
        print(f"Multiply Result: {result}")
        self.assertEqual(result, 12)

    def test_divide(self):
        result = self.calc.divide(18, 2)
        print(f"Divide Result: {result}")
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()