from Simple_Fun_170_Sum_Groups_6_kyu import sum_groups
import unittest

class Fun(unittest.TestCase):
    def test_1(self):
        data = [1, 1, 2, 2]
        result = 1
        self.assertEqual(sum_groups(data), result)
    
    def test_1(self):
        data = [2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]
        result = 6
        self.assertEqual(sum_groups(data), result)

if __name__ == '__main__':
    unittest.main()