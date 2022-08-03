from Write_number_in_expanded_form_6_kyu import expanded_form
import unittest

class Expanded(unittest.TestCase):
    def test_1(self):
        number = 12
        result = '10 + 2'
        self.assertEqual(expanded_form(number), result)
    
    def test2(self):
        number = 70304
        result = '70000 + 300 + 4'
        self.assertEqual(expanded_form(number), result)
        
if __name__ == "__main__":
    unittest.main()        
        
            