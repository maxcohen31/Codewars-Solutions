from Permutations_4_kyu import permutations
import unittest

class Perm(unittest.TestCase):
    def test_1(self):
        data = 'a'
        result = {'a'}
        self.assertEqual(permutations(data), result)
        
    def test_2(self):
        data = 'ab'    
        result = {'ab', 'ba'}
        self.assertEqual(permutations(data), result)
        
    def test_3(self):
        data = 'aabb'
        result = {'baba', 'aabb', 'baab', 'bbaa', 'abab', 'abba'}
        self.assertEqual(permutations(data), result)
        
        
if __name__ == "__main__":
    unittest.main()
    
        