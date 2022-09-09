import unittest
from Vowel_Count_7_kyu import get_count

class Count(unittest.TestCase):
    def test_1(self):
        data = 'Hello World'
        result = 3
        self.assertEqual(get_count(data), result)
    def test_2(self):    
        data = 'I love You'
        result = 4
        self.assertEqual(get_count(data), result)
        
if __name__ == "__main__":
    unittest.main()           