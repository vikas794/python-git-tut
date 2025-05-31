import unittest
from lib.math import factorial, fibonacci, is_prime, gcd, lcm, is_perfect_square

class TestMathFunctions(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(10), 55)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(-2))

    def test_gcd(self):
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(17, 23), 1)
        self.assertEqual(gcd(96, 64), 32)

    def test_lcm(self):
        self.assertEqual(lcm(12, 18), 36)
        self.assertEqual(lcm(17, 23), 17 * 23)
        self.assertEqual(lcm(5, 10), 10)
        self.assertEqual(lcm(0, 5), 0) # Based on common definition lcm(a,0) = 0

    def test_is_perfect_square(self):
        self.assertTrue(is_perfect_square(0))
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(4))
        self.assertTrue(is_perfect_square(9))
        self.assertTrue(is_perfect_square(16))
        self.assertFalse(is_perfect_square(2))
        self.assertFalse(is_perfect_square(3))
        self.assertFalse(is_perfect_square(5))
        self.assertFalse(is_perfect_square(-1))
        self.assertFalse(is_perfect_square(10))

if __name__ == '__main__':
    unittest.main()
