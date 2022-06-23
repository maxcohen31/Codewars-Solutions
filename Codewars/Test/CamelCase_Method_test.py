from CamelCase_Method_6_kyu import camel_case
import unittest

class CamelMeth(unittest.TestCase):
    def test_1(self):
        str_ = 'hello world'
        result = 'HelloWorld'
        self.assertEqual(camel_case(str_), result)
        
    def test_1(self):
        str_ = 'this is a test'
        result = 'ThisIsATest'
        self.assertEqual(camel_case(str_), result)
        
if __name__ == '__main__':
    unittest.main()