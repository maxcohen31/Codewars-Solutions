import unittest
from Roman_Numerals_Decoder_6_kyu import solution

class RomanNumerals(unittest.TestCase):
    def test_1(self):
        rom = 'IX'
        output = 9
        self.assertEqual(solution(rom), output)
    
    def test_2(self):
        rom = 'CDXLIII'
        output = 443
        self.assertEqual(solution(rom), output)
    
    def test_3(self):
        rom = 'MMXIX'
        output = 2019
        self.assertEqual(solution(rom), output)

if __name__ == '__main__':
    unittest.main()
