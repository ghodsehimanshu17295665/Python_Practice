import unittest
from sample_28 import add, subtract, divide


class TestSample(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)

        # Check for exception handling
        with self.assertRaises(ValueError):
            divide(10, 0)


# Running the tests
if __name__ == '__main__':
    unittest.main()
