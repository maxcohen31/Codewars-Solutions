from Find_the_unique_number_6_kyu import find_uniq
import unittest

class UniqueNumber(unittest.TestCase):
    def test_1(self):
        data = [1, 1, 3, 1, 1]
        result = 3
        self.assertEqual(find_uniq(data), result)
        
    def test_2(self):
        data = [0, 0, 0, 0.55, 0, 0 ,0]
        result = 0.55    
        self.assertEqual(find_uniq(data), result)
        
if __name__ == '__main__':
    unittest.main()        