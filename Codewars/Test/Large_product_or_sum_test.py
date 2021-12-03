import unittest
from Large_product_or_sum_7_kyu import sum_or_product

class SumPro(unittest.TestCase):
    def test_1(self):
        n = 3
        arr = [10, 41, 8, 16, 20, 36, 9, 13, 20]
        result = 'product'
        self.assertEqual(sum_or_product(arr, n), result)
    def test_2(self):
        n = 3
        arr = [-4, -1, 5, -7, -2, 6, 20, 23, 7]
        result = 'sum'
        self.assertEqual(sum_or_product(arr, n), result)    
    def test_3(self):
        n = 3
        arr = [10, 20, 3, 30, 5, 4]
        result = 'same'
        self.assertEqual(sum_or_product(arr, n), result)    
        
if __name__ == "__main__":
    unittest.main()