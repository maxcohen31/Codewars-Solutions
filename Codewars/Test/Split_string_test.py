import unittest
import Split_strings_6_kyu

class SplitTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(Split_strings_6_kyu.solution('Ciao Ema'), ['Ci', 'ao', 'Em', 'a'])
        
    def test_2(self):
        self.assertEqual(Split_strings_6_kyu.solution(''), [])
     
    def test_3(self):
        self.assertEqual(Split_strings_6_kyu.solution('Make my day'), ['Ma', 'ke', 'my', 'da', 'y_']) 
            
if __name__ == "__main__":
    unittest.main()        
        