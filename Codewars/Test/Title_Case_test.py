import unittest
from Title_Case_6_kyu import title_case

class TitleCase(unittest.TestCase):
    def test_1(self):
        data = 'a clash of KINGS'
        output = 'A Clash of Kings'
        minor_words = 'a an the of'
        self.assertEqual(title_case(data, minor_words), output)
    
    def test_1(self):
        data = 'THE WIND IN THE WILLOWS'
        output = 'The Wind in the Willows'
        minor_words = 'The In'
        self.assertEqual(title_case(data, minor_words), output)

if __name__ == '__main__':
    unittest.main()