from Alien_Beer_Morse_Code_6_kyu import morse_converter
import unittest

class Alien(unittest.TestCase):
    def test_1(self):
        message = "--...---.."
        result = 78
        self.assertEqual(morse_converter(message), result)
    
    def test_2(self):
        message = "---..-----...--"
        result = 803
        self.assertEqual(morse_converter(message), result)

if __name__ == "__main__":
    unittest.main()