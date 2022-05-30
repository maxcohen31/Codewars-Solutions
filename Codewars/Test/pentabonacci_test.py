from Pentabonacci_6_kyu import count_odd_pentaFib
import unittest

class Pentabonacci(unittest.TestCase):
    def test_1(self):
        n = 0
        result = 0
        self.assertEqual(count_odd_pentaFib(n), result)
        
    def test_1(self):
        n = 10
        result = 3
        self.assertEqual(count_odd_pentaFib(n), result)
    
    def test_1(self):
        n = 68
        result = 23
        self.assertEqual(count_odd_pentaFib(n), result)
        
if __name__ == '__main__':
    unittest.main()