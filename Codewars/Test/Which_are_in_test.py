import unittest
from Which_are_in_6_kyu import in_array

class ArrayWords(unittest.TestCase):
    def test_1(self):
        data = ["arp", "live", "strong"]
        data2 = ["lively", "alive", "harp", "sharp", "armstrong"]  
        result = ["arp", "live", "strong"]
        self.assertEqual(in_array(data, data2), result)
        
if __name__ == "__main__":
    unittest.main()        