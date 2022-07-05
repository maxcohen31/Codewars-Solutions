import unittest
from WeIrD_StRiNg_CaSe_6_kyu import to_weird_case

class WeirdStringCase(unittest.TestCase):
    def test_1(self):
        data = 'This is a test'
        output = 'ThIs Is A TeSt'
        self.assertEqual(to_weird_case(data), output)
    def test_1(self):
        data = 'This'
        output = 'ThIs'
        self.assertEqual(to_weird_case(data), output)

if __name__ == '__main__':
    unittest.main()
    