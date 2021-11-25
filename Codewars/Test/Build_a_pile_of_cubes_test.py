import unittest
from Build_a_pile_of_cubes_6_kyu import find_nb

class Cubes(unittest.TestCase):
    def test_1(self):
        m = 1071225
        result = 45
        self.assertEqual(find_nb(m), result)
    def test_2(self):
        m = 992324447
        result = -1
        self.assertEqual(find_nb(m), result)
       
if __name__ == "__main__":
    unittest.main()       
        
            