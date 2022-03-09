import unittest
from Prime_factors_6_kyu import prime_factors

class Factors(unittest.TestCase):
    def test(self):
        data = [(2, [2]), 
                (12, [2, 2, 3]),
                (100, [2, 2, 5, 5]),
                (230, [2, 5, 23]),
                (545, [5, 109]),
                (1456, [2, 2, 2, 2, 7, 13]),
                (5037, [3, 23, 73]),
                (15997,[17, 941]),
                (1234567890, [2, 3, 3, 5, 3607, 3803])
                ]
        
        for entry, result in data:
            self.assertEqual(prime_factors(entry), result)
            
            
if __name__ == "__main__":
    unittest.main()