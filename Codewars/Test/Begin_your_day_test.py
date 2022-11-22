from Begin_your_day_with_a_challenge_but_an_easy_one_6_kyu import one_two_three
import unittest

class Challenge(unittest.TestCase):
    def test_1(self):
        data = 3
        result = [3, 111]
        self.assertEqual(one_two_three(data), result)
    
    def test_2(self):
        data = 19
        result = [991, int(data * '1')]
        self.assertEqual(one_two_three(data), result)
    def test_1(self):
        data = 157
        result = [999999999999999994, int(data * '1')]
        self.assertEqual(one_two_three(data), result)
    

if __name__ == "__main__":
    unittest.main()