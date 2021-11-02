import unittest
from Double_char_8_kyu import double_char

class Double(unittest.TestCase):
    def test_1(self):
        data_test = [('abc', 'aabbcc'), ('String', 'SSttrriinngg')]
        for data, result in data_test:
            self.assertEqual(double_char(data), result)
            
if __name__ == "__main__":
    unittest.main()            
            