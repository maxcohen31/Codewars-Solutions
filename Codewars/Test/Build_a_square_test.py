import unittest
from Build_a_square_7_kyu import generate_shape

class Shape(unittest.TestCase):
    def test_1(self):
        n = 3
        result = '+++\n+++\n+++'
        self.assertEqual(generate_shape(n), result)
    def test_2(self):
        n = 5    
        result = '+++++\n+++++\n+++++\n+++++\n+++++'
        self.assertEqual(generate_shape(n), result)
        
if __name__ == "__main__":
    unittest.main()        