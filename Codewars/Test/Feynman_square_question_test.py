from Feynman_square_question_6_kyu import count_squares
import unittest

class Squares(unittest.TestCase):
    def test_1(self):
        n = 4
        result = 30
        self.assertEqual(count_squares(n), result)
    
    def test_1(self):
        n = 5
        result = 55
        self.assertEqual(count_squares(n), result)
    
    def test_1(self):
        n = 1000000
        result = 333333833333500000
        self.assertEqual(count_squares(n), result)
        
if __name__ == '__main__':
    unittest.main()