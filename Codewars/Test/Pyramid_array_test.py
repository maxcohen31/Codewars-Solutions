import unittest
from Pyramid_array_6_kyu import pyramid

class Pyramid(unittest.TestCase):
    def test_1(self):
        data = 0
        result = []
        self.assertEqual(pyramid(data), result)
    def test_2(self):    
        data = 3
        result = [[1], [1, 1], [1, 1, 1]]
        self.assertEqual(pyramid(data), result)
        
if __name__ == "__main__":
    unittest.main()           