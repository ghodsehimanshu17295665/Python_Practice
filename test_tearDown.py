import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()  # Set up a new Calculator instance for each test
        print("Setting up the calculator for testing.")

    def tearDown(self):
        print("Tearing down the calculator.")  # Clean up actions can go here
        del self.calc  # Delete the Calculator instance to clean up

    def test_add(self):
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
