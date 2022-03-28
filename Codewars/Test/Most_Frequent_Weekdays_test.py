from Most_Frequent_Weekdays_6_kyu import most_frequent_days
import unittest

class Days(unittest.TestCase):
    def test_1(self):
        year = 2000
        days = ['Saturday', 'Sunday']
        self.assertEqual(most_frequent_days(year), days)
        
    def test_2(self):
        year = 1770
        days = ['Monday']    
        self.assertEqual(most_frequent_days(year), days)

if __name__ == "__main__":
    unittest.main()