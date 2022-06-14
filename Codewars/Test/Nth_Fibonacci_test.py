import unittest
from Nth_Fibonacci_6_kyu import nth_fib

class Fibonacci(unittest.TestCase):
    def test_1(self):
        n = 2
        result = 4
        self.assertEqual(nth_fib(b), result)
        
    def test_1(self):
        n = 100
        result = 218922995834555169026
        self.assertEqual(nth_fib(b), result)
    
    def test_1(self):
        n = 43
        result = 267914296
        self.assertEqual(nth_fib(b), result)