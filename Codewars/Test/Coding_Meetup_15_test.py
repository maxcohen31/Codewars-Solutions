from Coding_Meetup_15_Higher_Order_Function_Series_FInd_the_odd_names import find_odd_names
import unittest

class OddNames(unittest.TestCase):
    def test_1(self):
        data = [
          { 'firstName': 'Aba', 'lastName': 'N.', 'country': 'Ghana', 'continent': 'Africa', 'age': 21, 'language': 'Python' },
          { 'firstName': 'Abb', 'lastName': 'O.', 'country': 'Israel', 'continent': 'Asia', 'age': 39, 'language': 'Java' }
        ]
        result = [{'firstName': 'Abb', 'lastName': 'O.', 'country': 'Israel', 'continent': 'Asia', 'age': 39, 'language': 'Java'}]
        self.assertEqual(find_odd_names(data), result)
        
        
if __name__ == '__main__':
    unittest.main()        