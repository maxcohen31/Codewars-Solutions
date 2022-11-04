import unittest
from Calculate_Variance_5_kyu import variance

class Variance(unittest.TestCase):
    def test_1(self):
        data = [1, 2, 2, 3]
        var = 0.5
        self.assertEqual(variance(data), var)
    
    def test_2(self):
        data = [12, 23, 65, 89, 94, 200]
        var = 3795.5833333333335
        self.assertEqual(variance(data), var)

if __name__ == '__main__':
    unittest.main()