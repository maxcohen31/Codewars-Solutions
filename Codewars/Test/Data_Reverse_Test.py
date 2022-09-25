import unittest
from Data_Reverse_6_kyu import data_reverse

class DataReverse(unittest.TestCase):
    def test_1(self):
        input_ = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
        result = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
        self.assertEqual(data_reverse(input_), result)

    def test_2(self):
        input_ = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
        result = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
        self.assertEqual(data_reverse(input_), result)

if __name__ == '__main__':
    unittest.main()