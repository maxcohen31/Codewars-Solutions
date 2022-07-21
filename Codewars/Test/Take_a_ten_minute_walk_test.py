import unittest
from Take_a_ten_minute_walk_6_kyu import is_valid_walk

class Walk(unittest.TestCase):
    def test_1(self):
        walk = ['n','s','n','s','n','s','n','s','n','s']     
        result = True
        self.assertEqual(is_valid_walk(walk), result)
    def test_2(self):
        walk = ['s']
        result = False
        self.assertEqual(is_valid_walk(walk), result)
    def test_3(self):
        walk = ['w','e','w','e','w','e','w','e','w','e','w','e']
        result = False
        self.assertEqual(is_valid_walk(walk), result)        
        
if __name__ == "__main__":
    unittest.main()        