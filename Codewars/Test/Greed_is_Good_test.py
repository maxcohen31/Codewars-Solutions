from Greed_is_Good_5_kyu import score
import unittest

class Greed(unittest.TestCase):
    def test_1(self):
        dices = [1, 1, 1 , 5, 3]
        output = 450
        self.assertEqual(score(dices), output)
    def test_1(self):
        dices = [2, 3, 4, 6, 2]
        output = 0
        self.assertEqual(score(dices), output)
    def test_1(self):
        dices = [1, 1, 1 , 3, 1]
        output = 1100
        self.assertEqual(score(dices), output)
        
if __name__ == '__main__':
    unittest.main()