import unittest
from Scramblies_5_kyu import scramble

class ScrambleTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(scramble('aloh', 'hola'), True)
    
    def test2(self):  
        self.assertEqual(scramble('aloh', ''), False)  
        
if __name__ == "__main__":
    unittest.main()        
        
        