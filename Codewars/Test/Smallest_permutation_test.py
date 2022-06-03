from Smallest_permutation_6_kyu import min_permutation
import unittest

class Permutation(unittest.TestCase):
    def test_1(self):
        data = -32
        result = -23
        self.assertEqual(min_permutation(data), result)
    
    def test_2(self):
        data = -2013022
        result = -1002223
        self.assertEqual(min_permutation(data), result)
    
    def test_3(self):
        data = 9125660530
        result = 1002355669
        self.assertEqual(min_permutation(data), result)
        
        
if __name__ == '__main__':
    unittest.main()