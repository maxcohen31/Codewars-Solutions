import unittest
from Grains_7_kyu import square

class Grains(unittest.TestCase):
    def test_1(self):
        data_test = [(1, 1), 
                     (2, 2),
                     (5, 16),
                     (15, 16384)
                     ]
        for data, result in data_test:
            self.assertEqual(square(data), result)
    
if __name__ == "__main__":
    unittest.main()            