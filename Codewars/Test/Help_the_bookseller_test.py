import unittest
from Help_the_bookseller_6_kyu import stock_list

class BookSeller(unittest.TestCase):
    def test_1(self):
        books = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        letters = ["A", "B"]
        result = '(A : 200) - (B : 1140)'
        self.assertEqual(stock_list(books, letters), result)
    
    def test_2(self):
        books = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        letters = ["N", "B", 'F']
        result = '(N : 0) - (B : 1140) - (F : 0)'
        self.assertEqual(stock_list(books, letters), result)
    
    def test_3(self):
        books = []
        letters = ["N", "B", 'F']
        result = ''
        self.assertEqual(stock_list(books, letters), result)

if __name__ == '__main__':
    unittest.main()