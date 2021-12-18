import unittest
from Powers_of_i_7_kyu import pofi

class Immaginary(unittest.TestCase):
    def test_1(self):
        n = 4
        power = '1'
        self.assertEqual(pofi(n), power)
    def test_1(self):
        n = 2
        power = '-1'
        self.assertEqual(pofi(n), power)    
    def test_1(self):
        n = 5
        power = 'i'
        self.assertEqual(pofi(n), power)    
    def test_1(self):
        n = 3
        power = '-i'
        self.assertEqual(pofi(n), power)    
        
if __name__ == "__main__":
    unittest.main()        