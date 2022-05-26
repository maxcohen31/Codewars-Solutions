from If_you_can_read_this_6_kyu import to_nato
import unittest

class Nato(unittest.TestCase):
    def test_1(self):
        data = '?ac'
        result = '? Alfa Charlie'
        self.assertEqual(to_nato(data), result)
        
    def test_2(self):
        data = 'If you can read this'
        result = 'India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta Tango Hotel India Sierra'
        self.assertEqual(to_nato(data), result)        
        
if __name__ == '__main__':
    unittest.main()