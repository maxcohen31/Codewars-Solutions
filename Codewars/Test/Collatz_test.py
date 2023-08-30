from Collatz_6_kyu import collatz
import unittest

class Collatz(unittest.TestCase):
    def test_1(self):
        n = 4
        result = "4->2->1"
        self.assertEqual(collatz(n), result)

    def test_2(self):
        n = 3
        result = "3->10->5->16->8->4->2->1"
        self.assertEqual(collatz(n), result)

if __name__ == "__main__":
    unittest.main()
