from Find_the_unique_string_5_kyu import find_uniq
import unittest

class UniqueString(unittest.TestCase):
    
    def test_1(self):
        data = ['aa', 'AAAaa', 'A', 'BbB', 'Aaa']
        result = 'BbB'
        self.assertEqual(find_uniq(data), result)
        
    def test_2(self):
        data = ['abc', 'cbc', 'bac', 'foo', 'acb', 'bca', 'cba']
        result = 'foo'    
        self.assertEqual(find_uniq(data), result)
    
    def test_3(self):
        data = [' ', 'X', ' ']
        result = 'X'
        self.assertEqual(find_uniq(data), result)
        
if __name__ == '__main__':
    unittest.main()        