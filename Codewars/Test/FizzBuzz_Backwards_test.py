import unittest
from FizzBuzz_backwards_6_kyu import reverse_fizz_buzz


class FizzBuzz(unittest.TestCase):
    def test_1(self):
        input = [1, 2, "Fizz", 4, "Buzz", 6] 
        result = (3, 5)
        self.assertEqual(reverse_fizz_buzz(input), result)
    
    def test_1(self):
        input = ["Fizz", "Fizz", "Fizz", "Fizz", "Fizz", "FizzBuzz"]
        result = (1, 6)
        self.assertEqual(reverse_fizz_buzz(input), result)

if __name__ == "__main__":
    unittest.main()