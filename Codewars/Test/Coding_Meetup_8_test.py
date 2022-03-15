from Coding_Meetup_8_Will_all_continents_be_represented_6_kyu import all_continents
import unittest

class Continent(unittest.TestCase):
    def test_1(self):
        data = [
            { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
            { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
            { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
            { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
        ]
        result = False
        self.assertEqual(all_continents(data), result)
        
 
if __name__ == "__main__":
    unittest.main()        