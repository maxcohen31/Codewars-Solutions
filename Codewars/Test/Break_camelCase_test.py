import unittest
from Break_camelCase_6_kyu import solution

class BreakingCase(unittest.TestCase):
    def test_1(self):
        data = 'helloWorld'
        result = 'hello World'
        self.assertEqual(solution(data), result)
        
    def test_2(self):
        data = 'breakCamelCase'
        result = 'break Camel Case'
        self.assertEqual(solution(data), result)
        
if __name__ == "__main__":
    unittest.main()        
            