import unittest
from Balanced_numbers_7_kyu import balanced_num

class BalancedNumber(unittest.TestCase):
    def test_1(self):
        self.assertEqual(balanced_num(295519), 'Not Balanced')
    def test_1(self):
        self.assertEqual(balanced_num(5), 'Balanced')
    def test_1(self):
        self.assertEqual(balanced_num(191), 'Balanced')    
                
if __name__ == '__main__':
    unittest.main()        