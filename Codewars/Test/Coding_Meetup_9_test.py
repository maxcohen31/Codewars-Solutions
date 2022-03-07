from Coding_Meetup_9_Age_diverse_6_kyu import is_age_diverse
import unittest

class AgeDiverse(unittest.TestCase):
    def test_1(self):
        data = [
            { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 19, 'language': 'Python' },
            { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 29, 'language': 'JavaScript' },
            { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
            { 'firstName': 'Noa', 'lastName': 'A.', 'country': 'Israel', 'continent': 'Asia', 'age': 40, 'language': 'Ruby' },
            { 'firstName': 'Andrei', 'lastName': 'E.', 'country': 'Romania', 'continent': 'Europe', 'age': 59, 'language': 'C' },
            { 'firstName': 'Maria', 'lastName': 'S.', 'country': 'Peru', 'continent': 'Americas', 'age': 60, 'language': 'C' },
            { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 75, 'language': 'Python' },
            { 'firstName': 'Chloe', 'lastName': 'K.', 'country': 'Guernsey', 'continent': 'Europe', 'age': 88, 'language': 'Ruby' },
            { 'firstName': 'Viktoria', 'lastName': 'W.', 'country': 'Bulgaria', 'continent': 'Europe', 'age': 98, 'language': 'PHP' },
            { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript' }
            ]
        result = True
        self.assertEqual(is_age_diverse(data), result)
        
    def test_2(self):
        data =  [
            { 'firstName': 'Thomas', 'lastName': 'K.', 'country': 'Germany', 'continent': 'Europe', 'age': 78, 'language': 'Python' },
            { 'firstName': 'Chen', 'lastName': 'T.', 'country': 'China', 'continent': 'Asia', 'age': 32, 'language': 'JavaScript' }    
        ]
        result = False
        self.assertEqual(is_age_diverse(data), result)
        

if __name__ == "__main__":
    unittest.main()        