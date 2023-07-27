from Transform_To_Prime_6_kyu import minimum_number
import unittest

class TransformPrime(unittest.TestCase):
    def test_1(self):
        n = [2, 5]
        result = 0
        self.assertEqual(minimum_number(n), result)
    
    def test_2(self):
        n = [2, 5, 10, 8, 2, 1, 4]
        result = 5
        self.assertEqual(minimum_number(n), result)
    
    

if __name__ == "__main__":
    unittest.main()
