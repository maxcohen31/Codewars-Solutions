from Reverse_Vowels_In_A_String_6_kyu import reverse_vowels
import unittest


class ReverseVowels(unittest.TestCase):
    def test_1(self):
        s = "Hello!"
        result = "Holle!"
        self.assertEqual(reverse_vowels(s), result)

    def test_2(self): 
        s = "Riverse Vowels in a String"
        result = "RivArsI Vewols en e Streng"
        self.assertEqual(reverse_vowels(s), result)


if __name__ == "__main__":
    unittest.main()
   

