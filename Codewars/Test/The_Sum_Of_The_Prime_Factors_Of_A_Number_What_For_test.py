from The_Sum_Of_The_Prime_Factors_Of_A_Number_What_For_6_kyu import is_prime, prime_factors, mult_primefactor_sum
import unittest

class SumFactors(unittest.TestCase):
    def test_1(self):
        a = 10
        b = 100
        result = [16, 27, 30, 60, 70, 72, 84]
        self.assertEqual(mult_primefactor_sum(a, b), result)
    
    def test_2(self):
        a = 1500
        b = 3002
        result = [1530, 1581, 1748, 1755, 1776, 1798, 1824, 1976, 2079, 2106, 2322, 2408, 2464, 2484, 2520, 2625, 2660, 2688, 2720, 2730, 2772, 2800, 2958, 2964, 2967, 2970, 3000]
        self.assertEqual(mult_primefactor_sum(a, b), result)


if __name__ == "__main__":
    unittest.main()