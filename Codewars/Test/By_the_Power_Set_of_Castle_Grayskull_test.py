from By_the_Power_Set_of_Castle_Grayskull_5_kyu import power
import unittest

class Subset(unittest.TestCase):
    def test_1(self):
        s = [1, 2, 3]
        result = [[], (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
        self.assertEqual(power(s), result)
    
    def test_2(self):
        s = [1, 2, 3, 4]
        result = [[], (1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4), (1, 2, 3, 4)]
        self.assertEqual(power(s), result)

if __name__ == "__main__":
    unittest.main()