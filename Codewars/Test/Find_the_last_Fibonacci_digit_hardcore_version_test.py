from Find_the_last_Fibonacci_digit_hardcore_version_6_kyu import last_fib_digit
import unittest

class Fibonacci(unittest.TestCase):
    def test_1(self):
        n = 7000006
        result = 3
        self.assertEqual(last_fib_digit(n), result)
    def test_1(self):
        n = 9000000008
        result = 4
        self.assertEqual(last_fib_digit(n), result)    

if __name__ == "__main__":
    unittest.main()