import unittest
from prime_18 import check_prime


class TestCheckPrime(unittest.TestCase):

    def test_prime_number(self):
        self.assertTrue(check_prime(2))
        self.assertTrue(check_prime(3))
        self.assertTrue(check_prime(11))
        self.assertTrue(check_prime(13))
        self.assertTrue(check_prime(17))

    def test_non_prime_number(self):
        self.assertFalse(check_prime(1))
        self.assertFalse(check_prime(4))
        self.assertFalse(check_prime(10))
        self.assertFalse(check_prime(16))
        self.assertFalse(check_prime(50))

    def test_edge_cases(self):
        self.assertFalse(check_prime(0))
        self.assertFalse(check_prime(-5))
        self.assertFalse(check_prime(-1))


if __name__ == '__main__':
    unittest.main()
