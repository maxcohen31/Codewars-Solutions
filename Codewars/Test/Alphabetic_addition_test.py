import unittest
from Alphabetic_addition_7_kyu import add_letters

class AlphaAdd(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add_letters('a', 'b'), 'c')
        
    def test_2(self):
        self.assertEqual(add_letters('z', 'c'), 'c')    
    
    def test_3(self):
        self.assertEqual(add_letters(), 'z')
        
if __name__ == '__main__':
    unittest.main()       