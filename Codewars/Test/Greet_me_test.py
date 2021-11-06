import unittest
from Greet_me_7_kyu import greet

class Greet(unittest.TestCase):
    def test_1(self):
        data_test = (
                     ['VALERIE', 'Hello Valerie!'],
                     ['krissy', 'Hello Krissy!'],
                     ['Brian', 'Hello Brian!']
                     )
        for data, result in data_test:
            self.assertEqual(greet(data), result)

if __name__ == "__main__":
    unittest.main()        
        
        
        