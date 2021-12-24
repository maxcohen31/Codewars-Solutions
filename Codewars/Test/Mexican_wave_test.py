import unittest
from Mexican_wave_6_kyu import wave

class MexicanWave(unittest.TestCase):
    def test_1(self):
        people = 'hello'
        result = ['Hello', 'hEllo', 'heLlo', 'helLo', 'hellO']
        self.assertEqual(wave(people), result)
    def test_2(self):
        people = 'codewars'
        result = ['Codewars', 'cOdewars', 'coDewars', 'codEwars', 'codeWars', 'codewArs', 'codewaRs', 'codewarS']
        self.assertEqual(wave(people), result)
        
if __name__ == "__main__":
    unittest.main()        
        