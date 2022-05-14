from Numerical_palindrome_1_5_6_kyu import palindrome
import unittest


class PalindromeList(unittest.TestCase):
    def test_1(self):
        start = 6
        range_ = 4
        result = [11, 22, 33, 44]
        self.assertEqual(palindrome(start, range_), result) 
    
    def test_2(self):
        start = 474
        range_ = 0
        result = [474]
        self.assertEqual(palindrome(start, range_), result)
    
    def test_3(self):
        start = 6
        range_ = -4
        result = 'Not valid'
        self.assertEqual(palindrome(start, range_), result)    
    
    def test_4(self):
        start = '6'
        range_ = 4
        result = 'Not valid'
        self.assertEqual(palindrome(start, range), result)
        
if __name__ == '__main__':
    unittest.main()        