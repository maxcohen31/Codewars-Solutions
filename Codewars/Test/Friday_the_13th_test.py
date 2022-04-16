import unittest
from Friday_the_13th_6_kyu import friday_the_thirteenths

class Friday(unittest.TestCase):
    def test_1(self):
        start = 2000
        end = None
        result = '10/13/2000'
        self.assertEqual(friday_the_thirteenths(start, end), result)
    
    def test_2(self):
        start = 1999
        end = 2000
        result = '8/13/1999 10/13/2000'
        self.assertEqual(friday_the_thirteenths(start, end), result)
    
if __name__ == '__main__':
    unittest.main()