import unittest
from The_Enigma_Machine_the_plugboard_6_kyu import Plugboard

class Enigma(unittest.TestCase):
    def test_1(self):
        p = Plugboard('ABCD')
        input_ = p.process('A')
        output = 'B'
        self.assertEqual(input_, output)
        
    def test_2(self):
        p = Plugboard('ABCD')
        input_ = p.process('.')
        output = '.'
        self.assertEqual(input_, output)
        
if __name__ == '__main__':
    unittest.main()