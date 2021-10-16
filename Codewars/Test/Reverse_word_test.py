import unittest
import Reverse_words_7_kyu

class TestReverse(unittest.TestCase):
    def test_one(self):
        self.assertEqual("sihT si na !elpmaxe", Reverse_words_7_kyu.reverse_words("This is an example!"))

if __name__== "__main__":
    unittest.main()
    