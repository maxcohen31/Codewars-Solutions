import unittest
from Sum_Of_Parts_6_kyu import parts_sums

class PartsSum(unittest.TestCase):
    def test_1(self):
        input_ = [0, 1, 3, 6, 10]
        output = [20, 20, 19, 16, 10, 0]
        self.assertEqual(parts_sums(input_), output)

    def test_2(self):
        input_ = [1, 2, 3, 4, 5, 6]
        output = [21, 20, 18, 15, 11, 6, 0]
        self.assertEqual(parts_sums(input_), output)

if __name__ == '__main__':
    unittest.main()

