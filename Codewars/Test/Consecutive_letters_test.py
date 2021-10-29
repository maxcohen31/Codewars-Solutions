import unittest
from Consecutive_letters_7_kyu import solve

class ConsecutiveLetters(unittest.TestCase):
    def test(self):
        data_test = [
                 ('a', True),
                 ('abc', True),
                 ('', True),
                 ('abbc', False),
                 ('bdgf', False)
                ]
        for data, result in data_test:
            self.assertEqual(solve(data), result)        
        
if __name__ == "__main__":
    unittest.main()        
        
    