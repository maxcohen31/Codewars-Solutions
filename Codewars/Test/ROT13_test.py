import unittest
from ROT13_5_kyu import rot13

class Rot(unittest.TestCase):
    def test_1(self):
        self.assertEqual(rot13('ROT13 example.'), 'EBG13 rknzcyr.')
    def test_2(self):
        self.assertEqual(rot13('#--#'), '#--#')
    def test_3(self):    
        data = "How can you tell an extrovert from an introvert at NSA?Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf."
        result = "Ubj pna lbh gryy na rkgebireg sebz na vagebireg ng AFN?In the elevators, the extrovert looks at the OTHER guy's shoes."
        self.assertEqual(rot13(data), result) 
                                
            
if __name__ == "__main__":
    unittest.main()            