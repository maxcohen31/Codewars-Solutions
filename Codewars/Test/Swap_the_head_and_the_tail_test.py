import unittest
from Swap_the_head_and_the_tail_7_kyu import swap_head_tail

class Swap(unittest.TestCase):
    def test_1(self):
        data = [1, 2, 3]
        result = [3, 2, 1]
        self.assertEqual(swap_head_tail(data), result)
    def test_2(self):    
        data = [6, 7, 8, 9, 10, 12]
        result = [9, 10, 12, 6, 7, 8]
        self.assertEqual(swap_head_tail(data), result)
        
if __name__ == "__main__":
    unittest.main()           