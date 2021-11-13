import unittest
from Character_counter_7_kyu import validate_word

class Counter(unittest.TestCase):
    def test_1(self):
        data_test = [('Hello', False),
                     ('AbccIEr', False),
                     ('Acbacb', True)
                     ]
        for data, result in data_test:
            self.assertEqual(validate_word(data), result)
            
            
if __name__ == "__main__":
    unittest.main()            