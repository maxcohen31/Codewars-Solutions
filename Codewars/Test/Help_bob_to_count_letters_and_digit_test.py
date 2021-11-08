import unittest
from Help_bob_to_count_letters_and_digits_7_kyu import count_letters_and_digits

class HelpBob(unittest.TestCase):
    def test(self):
        test = [('A!!', 1), ('wicked!!-', 6), ('', 0)]
        for expect, result in test:
            self.assertEqual(count_letters_and_digits(expect), result)
            
            
if __name__ == '__main__':
    unittest.main()            