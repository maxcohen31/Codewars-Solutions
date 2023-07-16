from Ready_For_Prime_Time_5_kyu import prime, is_prime
import unittest

class Prime(unittest.TestCase):
    def test_1(self):
        n = 5
        result = [2, 3, 5]
        self.assertEqual(prime(n), result)

    def test_2(self):
        n = 11
        result = [2, 3, 5, 7, 11]
        self.assertEqual(prime(n), result)

if __name__ == "__main__":
    unittest.main()