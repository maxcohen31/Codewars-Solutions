import unittest
import Maximum_product_7_kyu

class MaxProTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Maximum_product_7_kyu.adjacent_element_product([1, 2, 3, 1]), 6)
    def test_1(self):
        self.assertEqual(Maximum_product_7_kyu.adjacent_element_product([1, 2]), 2)      
        
if __name__== "__main__":
    unittest.main()        