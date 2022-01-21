import unittest
from Multiplication_tables_6_kyu import multiplication_table

class Table(unittest.TestCase):
    def test_1(self):
        input_ = 2
        output = [[1, 2], [2, 4]]
        self.assertEqual(multiplication_table(input_), output)
    def test_2(self):
        input_ = 3
        output = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]    
        self.assertEqual(multiplication_table(input_), output)
    def test_3(self):
        input_ = 5
        output = [
                  [1, 2, 3, 4, 5], 
                  [2, 4, 6, 8, 10], 
                  [3, 6, 9, 12, 15], 
                  [4, 8, 12, 16, 20], 
                  [5, 10, 15, 20, 25]
                  ]
        self.assertEqual(multiplication_table(input_), output)
        
        
if __name__ == "__main__":
    unittest.main()        