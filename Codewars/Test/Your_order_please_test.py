from Your_order_please_6_kyu import order
import unittest

class Order(unittest.TestCase):
    def test_1(self):
        data = "is2 Thi1s T4est 3a"
        result = "Thi1s is2 3a T4est"
        self.assertEqual(order(data), result)
        
    def test_2(self):
        data = "W0uld Valentin5e b2 m4 you2"    
        result = "W0uld you1 b2 m4 Valentin5e"
        self.assertEqual(order(data), result)
        
        