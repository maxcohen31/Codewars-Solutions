import unittest
from SumFibs_6_kyu import sum_fibs

class Fibo(unittest.TestCase):
    def test_1(self):
        n = 5
        result = 2
        self.assertEqual(sum_fibs(n), result)
    def test_2(self):
        n = 10
        result = 44
        self.assertEqual(sum_fibs(n), result)
      
if __name__ == "__main__":
    unittest.main()