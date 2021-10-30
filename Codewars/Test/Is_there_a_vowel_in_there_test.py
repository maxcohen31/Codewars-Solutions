import unittest
from Is_there_a_vowel_in_there_6_kyu import is_vow

class Vowel(unittest.TestCase):
    def test_1(self):
        data = [100, 100, 116, 105, 117, 121]
        result = [100, 100, 116, 'i', 'u', 121]
        self.assertEqual(is_vow(data), result) 
    
    def test_2(self):
        data = [118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ]
        result = [118, 117, 120, 121, 117, 98, 122, 97, 120, 106, 104, 116, 113, 114, 113, 120, 106]  
        self.assertEqual(is_vow(data), result)

if __name__ == "__main__":
    unittest.main()        