import unittest
from Good_Vs_Evil_6_kyu import good_vs_evil

class LOTR(unittest.TestCase):
    def test_1(self):
        data1, data2 = '0 0 0 0 0 10', '0 1 1 1 1 0 0'
        output = 'Battle Result: Good triumphs over Evil'
        self.assertEqual(good_vs_evil(data1, data2), output)
        
    def test_2(self):
        data1, data2 = '0 1 0 4 0 10', '0 1 1 1 4 0 10'
        output = 'Battle Result: Evil eradicates all trace of Good'
        self.assertEqual(good_vs_evil(data1, data2), output)
        
    def test_3(self):
        data1, data2 = '0 0 0 0 0 10', '0 0 0 0 0 0 10'
        output = 'Battle Result: No victor on this battle field'
        self.assertEqual(good_vs_evil(data1, data2), output)
        
if __name__ == '__main__':
    unittest.main()