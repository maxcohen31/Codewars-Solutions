import unittest
from Equal_Side_of_an_array_6_kyu import find_even_index


class EqualSide(unittest.TestCase):
    def test_1(self):
        arr = [1, 2, 3, 4, 3, 2, 1]
        result = 4
        self.assertEqual(find_even_index(arr), result)

    def test_2(self):
        arr = [0,0,0,0,0]
        result = 0
        self.assertEqual(find_even_index(arr), result)

    def test_3(self):
        arr = [100, -1]
        result = -1
        self.assertEqual(find_even_index(arr), result)

if __name__ == "__main__":
    unittest.main()