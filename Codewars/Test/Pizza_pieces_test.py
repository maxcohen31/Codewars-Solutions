import unittest
from Pizza_pieces_6_kyu import max_pizza

class Pizza(unittest.TestCase):
    def test_1(self):
        cuts = 3
        pieces = 7
        self.assertEqual(max_pizza(cuts), pieces)
    def test_1(self):
        cuts = 2
        pieces = 4
        self.assertEqual(max_pizza(cuts), pieces)    
 
if __name__ == "__main__":
    unittest.main()        