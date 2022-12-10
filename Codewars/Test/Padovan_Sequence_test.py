import unittest
from Padovan_Sequence_6_kyu import padovan

class Padovan(unittest.TestCase):
    def test_1(self):
        data  = [
            (1, 1),
            (1, 1),
            (6, 4),
            (7, 5),
            (12,21)
        ]
        for n, result in data:
            self.assertEqual(padovan(n), result)

if __name__ == "__main__":
    unittest.main()