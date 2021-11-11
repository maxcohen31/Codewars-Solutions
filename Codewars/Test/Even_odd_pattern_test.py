import unittest
from Even_odd_pattern_6_kyu import even_odd

class EvenOdd(unittest.TestCase):
    def test_1(self):
        lst = [1, 2, 3]
        result = 5
        self.assertEqual(even_odd(lst), result) 
        
    def test_2(self):
        lst = [1, 2, 2, 1, 6, 1, 3, 9, 6, 1]
        result = 123    
        self.assertEqual(even_odd(lst), result)
        
if __name__ == "__main__":
    unittest.main()        