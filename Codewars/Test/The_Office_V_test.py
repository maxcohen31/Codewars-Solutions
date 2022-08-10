from The_Office_V_Find_a_Chair_6_kyu import meeting
import unittest

class Office(unittest.TestCase):
    def test_1(self):
        data = [["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9]]
        need = 4
        result = [0, 1, 3]
        self.assertEqual(meeting(data, need), result)

    def test_2(self):
        data = [["XXX", 1], ["XXXXXX", 6], ["X", 2], ["XXXXXX", 8], ["X", 3], ["XXX", 1]]
        need = 5
        result = [0, 0, 1, 2, 2]
        self.assertEqual(meeting(data, need), result)

if __name__ == '__main__':
    unittest.main()