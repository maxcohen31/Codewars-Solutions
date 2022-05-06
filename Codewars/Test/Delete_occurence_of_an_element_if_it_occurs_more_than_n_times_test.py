import unittest
from Delete_occurence_of_an_element_if_it_occurs_more_than_n_times_6_kyu import delete_nth

class DeleteOccurence(unittest.TestCase):
    def test_1(self):
        data = [20, 37, 20, 21]
        result = [20, 37, 21]
        max_e = 1
        self.assertEqual(delete_nth(data, max_e), result)
    
    def test_2(self):
        data = [1,1,3,3,7,2,2,2,2]
        result = [1,1,3,3,7,2,2,2]
        max_e = 3
        self.assertEqual(delete_nth(data, max_e), result)
    
if __name__ == '__main__':
    unittest.main()