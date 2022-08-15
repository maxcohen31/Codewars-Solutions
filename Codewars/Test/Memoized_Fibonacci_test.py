from Memoized_Fibonacci_5_kyu import fibonacci
import unittest

class Fibo(unittest.TestCase):
    def test_1(self):
        n = 50
        output = 12586269025
        self.assertEqual(fibonacci(n), output)
    def test_2(self):
        n = 100
        output = 354224848179261915075
        self.assertEqual(fibonacci(n), output)
        
if __name__ == '__main__':
    unittest.main()