import unittest
from Array_leaders_array_series_3_ import array_leaders2

class Array_Leader(unittest.TestCase):
    def test_1(self):
        self.assertEqual(array_leaders2([0, -29, 3]), [0, 3])
    
    def test_2(self):
        self.assertEqual(array_leaders2([0,1, 2, 3, 4]), [4])    

if __name__ == '__main__':
    unittest.main()       