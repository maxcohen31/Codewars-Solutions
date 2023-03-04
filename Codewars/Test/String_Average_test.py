from String_Average_6_kyu import average_string
import unittest

class StringAvg(unittest.TestCase):
    def test_1(self):
        s = "one one eight one"
        result = "two"
        self.assertEqual(average_string(s), result)
    def test_1(self):
        s = "zero nine five one"
        result = "four"
        self.assertEqual(average_string(s), result)
    def test_1(self):
        s = ""
        result = "n/a"
        self.assertEqual(average_string(s), result)

if __name__ == "__main__":
    unittest.main()