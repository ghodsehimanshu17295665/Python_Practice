import unittest


class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This method is called before each test method
        self.calc = Calculator()  # Create an instance of the Calculator class
        print("Setting up the calculator for testing.")

    def test_add(self):
        result = self.calc.add(3, 5)  # Test the add method
        self.assertEqual(result, 8)    # Assert the expected outcome

    def test_subtract(self):
        result = self.calc.subtract(10, 4)  # Test the subtract method
        self.assertEqual(result, 6)          # Assert the expected outcome


if __name__ == '__main__':
    unittest.main()
