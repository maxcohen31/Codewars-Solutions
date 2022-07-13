import unittest
from Strip_Comments_4_kyu import solution

class Strip(unittest.TestCase):
    def test_1(self):
        data = "apples, pears # and bananas\ngrapes\nbananas !apples" 
        markers = ["#", "!"]
        sol = 'apples, pears\ngrapes\nbananas'
        self.assertEqual(solution(data, markers), sol)
        
if __name__ == '__main__':
    unittest.main()    