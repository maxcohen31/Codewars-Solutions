import unittest
from Sum_of_angles_7_kyu import angle

class AngleTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(angle(5), 540)
     
    def test_2(self):
        self.assertEqual(angle(3), 180) 
        
if __name__=='__main__':
    unittest.main()        