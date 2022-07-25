from The_Vowel_Code_6_kyu import encode, decode
import unittest

class Vowel(unittest.TestCase):
    def test_1(self):
        data = 'hello'
        result = 'h2ll4'
        self.assertEqual(encode(data), result)
    
    def test_1(self):
        data = 'h2ll4'
        result = 'hello'
        self.assertEqual(decode(data), result)
        
if __name__ == '__main__':
    unittest.main()