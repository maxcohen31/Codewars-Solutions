import unittest
from Integer_with_the_longest_Collatz_sequence_6_kyu import longest_collatz

class Collatz(unittest.TestCase):
    def test_1(self):
        input = [2, 4, 3]
        result = 3
        self.assertEqual(longest_collatz(input), result)

    def test_2(self):
        input = [2, 5, 32]
        result = 5
        self.assertEqual(longest_collatz(input), result)

if __name__ == "__main__":
    unittest.main()


