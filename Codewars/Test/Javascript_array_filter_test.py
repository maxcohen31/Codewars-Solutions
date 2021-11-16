import unittest
from Javascript_array_filter_7_kyu import get_even_numbers

class Filter(unittest.TestCase):
    def test_1(self):
        arr = [2, 4, 5]
        result = [2, 4]
        self.assertEqual(get_even_numbers(arr), result)   
    def test_2(self):
        arr = []
        result = []
        self.assertEqual(get_even_numbers(arr), result)
        
if __name__ == "__main__":
    unittest.main()            