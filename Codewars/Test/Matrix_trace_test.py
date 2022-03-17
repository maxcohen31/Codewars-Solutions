import unittest
from Matrix_trace_6_kyu import trace

class Trace(unittest.TestCase):
    def test_1(self):
        data = [[0, 0], [0, 0]]
        result = 0
        self.assertEqual(trace(data), result)
        
    def test_2(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = 15
        self.assertEqual(trace(data), result)
        
    def test_3(self):
        data = []
        result = None
        self.assertEqual(trace(data), result)
        
        
if __name__ == "__main__":
    unittest.main()                