from Ore_Numbers_6_kyu import is_ore
import unittest

class Ore(unittest.TestCase):
    def test_1(self):
        n = 6
        result = True
        self.assertEqual(is_ore(n), result)

    def test_2(self):
        n = 10
        result =False
        self.assertEqual(is_ore(n), result)

if __name__ == "__main__":
    unittest.main() 
 
