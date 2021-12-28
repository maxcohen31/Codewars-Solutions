import unittest
from random import randint
from Compare_powers_6_kyu import compare_powers


class Powers(unittest.TestCase):
    def test_1(self):
        a = [2, 5]
        b = [3, 9]
        result = 1
        self.assertEqual(compare_powers(a, b), result)
    def test_2(self):
        a = [33, 99]
        b = [22, 99]
        result = -1
        self.assertEqual(compare_powers(a, b), result)
    def test_3(self): 
        a = [2, 5]
        b = [2, 5]
        result = 0
        self.assertEqual(compare_powers(a, b), result)      
            
if __name__ == "__main__":
    unittest.main()        
        
        