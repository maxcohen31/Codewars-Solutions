from Matrix_transpose_6_kyu import transpose
import unittest

class Transpose(unittest.TestCase):
    def test_1(self):
        data = [
                [1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]
                ]   
        result = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(transpose(data), result)
        
    def test_2(self):
        data = [[1, 2, 3]]
        result = [[1], [2], [3]]
        self.assertEqual(transpose(data), result)
 
if __name__ == "__main__":
    unittest.main()        
        
            