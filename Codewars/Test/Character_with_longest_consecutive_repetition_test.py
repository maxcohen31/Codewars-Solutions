import unittest
from Character_with_longest_consecutive_repetiition_6_kyu import longest_repetition

class LongestRepetition(unittest.TestCase):
    def test(self):
        data = [
            ["zzzzcaszz", ('z', 4)],
            ["ba", ('b', 1)],
            ["", ('', 0)],
            ["22222sadfsafkkkkk", ('2', 5)]
        ]
        
        for chars, result in data:
            self.assertEqual(longest_repetition(chars), result)

if __name__ == "__main__":
    unittest.main()