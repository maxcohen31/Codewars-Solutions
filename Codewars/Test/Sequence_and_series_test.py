import unittest
from Sequence_and_series_6_kyu import get_score

class Score(unittest.TestCase):
    def test_1(self):
        n = 1
        result = 50
        self.assertEqual(get_score(n), result)
        
    def test_2(self):
        n = 3    
        result = 300
        self.assertEqual(get_score(n), result)
        
if __name__ == "__main__":
    unittest.main()        