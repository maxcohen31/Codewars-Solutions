import unittest
from Meeting_6_kyu import meeting

class Meet(unittest.TestCase):
    def test_1(self):
        data = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
        result = "(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
        self.assertEqual(meeting(data), result)
        
        
if __name__ == "__main__":
    unittest.main()        