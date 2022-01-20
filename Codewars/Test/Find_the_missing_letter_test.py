import unittest
from Find_the_missing_letter_6_kyu import find_missing_letter


class Letter(unittest.TestCase):
    def test_1(self):
        data = ["a", "b", "c", "d", "f"]
        result = "e"
        self.assertEqual(find_missing_letter(data), result)
        
    def test_2(self):
        data = ["A", "C"]
        result = "B"    
        self.assertEqual(find_missing_letter(data), result)
  
if __name__ == "__main__":
    unittest.main()        