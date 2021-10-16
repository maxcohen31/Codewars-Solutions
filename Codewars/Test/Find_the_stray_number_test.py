import unittest
import Find_the_stray_number_7_kyu

class TestStray(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Find_the_stray_number_7_kyu.stray([1, 1, 3]), 3)
        
    def test_2(self):
        self.assertEqual(Find_the_stray_number_7_kyu.stray([]), None)
        
if __name__ == "__main__":
    unittest.main()       
        