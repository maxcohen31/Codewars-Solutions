import unittest
from RGB_to_Hex_Convertion_5_kyu import rgb

class RGB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(rgb(255, 255, -4), 'FFFF00')
    
    def test_2(self):
        self.assertEqual(rgb(-255, 34, -4), '002200')
    
    def test_3(self):
        self.assertEqual(rgb(24, 33, 666), '1821FF')
    
if __name__ == '__main__':
    unittest.main()