import unittest
from Replace_with_alphabet_position_6_kyu import alphabet_position

class LetterPosition(unittest.TestCase):
    def test_1(self):
        string = 'Hello World!'
        result = '8 5 12 12 15 23 15 18 12 4'
        self.assertEqual(alphabet_position(string), result)
    def test_2(self):
        string = 'Give me a bottle of rum, you fuck'
        result = '7 9 22 5 13 5 1 2 15 20 20 12 5 15 6 18 21 13 25 15 21 6 21 3 11'
        self.assertEqual(alphabet_position(string), result)   
    def test_3(self):
        string = ''
        result = ''
        self.assertEqual(alphabet_position(string), result)
    def test_4(self):
        string = "Five o' clock"
        result = '6 9 22 5 15 3 12 15 3 11'
        self.assertEqual(alphabet_position(string), result)    
        
if __name__ == "__main__":
    unittest.main()        