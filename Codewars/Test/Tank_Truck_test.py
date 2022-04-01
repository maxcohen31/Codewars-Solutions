from Tank_Truck_6_kyu import tankvol
import unittest

class Volume(unittest.TestCase):
    def test_1(self):
        h, d, vt = 40, 120, 3500
        result = 1021
        self.assertEqual(tankvol(h, d, vt), result)
    def test_2(self):
        h, d, vt = 5, 7, 3848
        result = 2940
        self.assertEqual(tankvol(h, d, vt), result)
        
        
if __name__ == "__main__":
    unittest.main()        
