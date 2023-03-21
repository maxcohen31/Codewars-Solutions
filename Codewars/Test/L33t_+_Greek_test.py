from L33T_+_Grεεκ_Case_6_kyu import gr33k_l33t
from unittest import TestCase, main

class LeetGreek(TestCase):
    def test_1(self):
        string = "Codewars"
        result = "cθδεωαπs"
        self.assertEqual(gr33k_l33t(string), result)
    def test_1(self):
        string = "kata"
        result = "κατα"
        self.assertEqual(gr33k_l33t(string), result)
    def test_1(self):
        string = "kumite"
        result = "κμmιτε"
        self.assertEqual(gr33k_l33t(string), result)

if __name__ == "__main__":
    main()