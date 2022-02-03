import unittest
from Multiples_of_3_and_5_redux import solution

class Multiplies(unittest.TestCase):
    def test_1(self):
        n = 10
        result = 23
        self.assertEqual(solution(n), result)
    def test_1(self):
        n = 50000000000000000000000000000000000000000000000
        result = 58333333333333333333333333333333333333333333329
        1666666666666666666666666666666666666666666668
        self.assertEqual(solution(n), result)    
        
if __name__ == "__main__":
    unittest.main()        