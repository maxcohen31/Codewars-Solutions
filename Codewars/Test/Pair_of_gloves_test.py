import unittest
from Pair_of_gloves_6_kyu import number_of_pairs

class Gloves(unittest.TestCase):
    def test_1(self):
        data = ["red","green","blue"]
        result = 0
        self.assertEqual(number_of_pairs(data), result)
        
    def test_2(self):
        data = ["gray","black","purple","purple","gray","black", 'black']
        result = 3
        self.assertEqual(number_of_pairs(data), result)
        
if __name__ == '__main__':
    unittest.main()