import unittest
from Fibonacci_Rabbits_6_kyu import fib_rabbits

class FiboRabbits(unittest.TestCase):
    def test_1(self):
        n = 5
        b = 3
        result = 19
        self.assertEqual(fib_rabbits(n, b), result)
        
    def test_2(self):
        n = 8
        b = 12
        result = 8425
        self.assertEqual(fib_rabbits(n, b), result)
        
if __name__ == '__main__':
    unittest.main()
        