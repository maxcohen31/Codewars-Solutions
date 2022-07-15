import unittest
from Simple_division_6_kyu import solve

class Solve(unittest.TestCase):
    def test(self):
        data = [
                (15, 12, False),
                (2, 243, False),
                (4, 256, True),
                (2, 256, True)
                ]
        for a, b, c in data:
            self.assertEqual(solve(a, b), c)
    
if __name__ == "__main__":
    unittest.main()    
    
