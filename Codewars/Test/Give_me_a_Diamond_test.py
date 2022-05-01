from Give_me_a_Diamond_6_kyu import diamond
import unittest

class DiamondShape(unittest.TestCase):
    def test_1(self):
        n = 1
        result = '*\n'
        self.assertEqual(diamond(n), result)
    def test_2(self):
        n = 5
        result = "  *\n ***\n*****\n ***\n  *\n"
        self.assertEqual(diamond(n), result)
    def test_3(self):
        n = 0
        result = None
        self.assertEqual(diamond(n), result)
    
if __name__ == '__main__':
    unittest.main()