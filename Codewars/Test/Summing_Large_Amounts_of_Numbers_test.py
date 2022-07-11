from Summing_Large_Amounts_Of_Numbers_6_kyu import sum_them
import unittest

class SummingLargeNumbers(unittest.TestCase):
    def test_1(self):
        n = 0
        result = 0
        self.assertEqual(sum_them(n), result)
        
    def test_2(self):
        n = 2
        result = 6
        self.assertEqual(sum_them(n), result)
    
    def test_1(self):
        n = 12
        result = 8386560
        self.assertEqual(sum_them(n), result)
        
if __name__ == '__main__':
    unittest.main()