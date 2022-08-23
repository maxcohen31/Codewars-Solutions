from Two_Sum_6_kyu import two_sum
import unittest

class TwoSum(unittest.TestCase):
    def test_1(self):
        data = [1, 2, 3,]
        target = 4
        result = [0, 2]
        self.assertEqual(two_sum(data, target), result)
        
    def test_2(self):
        data = [1, 3, 5, 6]
        target = 8
        result = [1, 2]
        self.assertEqual(two_sum(data, target), result) 
        
if __name__ == '__main__':
    unittest.main()        