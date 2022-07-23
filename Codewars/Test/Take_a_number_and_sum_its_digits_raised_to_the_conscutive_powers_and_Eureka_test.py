import unittest
from Take_a_number_and_sum_its_digits_raised_to_the_consecutive_powers_and_Eureka_6_kyu import sum_dig_pow

class Eureka(unittest.TestCase):
    def test_1(self):
        a = 1
        b = 100
        result = [1, 2, 3, 4, 5, 6, 7 ,8, 9, 89]
        self.assertEqual(sum_dig_pow(a, b), result)
    
    def test_2(self):
        a = 1
        b = 10000000
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 598, 1306, 1676, 2427]
        self.assertEqual(sum_dig_pow(a, b), result)
        
if __name__ == "__main__":
    unittest.main()        