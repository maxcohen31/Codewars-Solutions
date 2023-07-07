from Dividers_of_Primes_6_kyu import get_dividers
from unittest import main, TestCase

class DivPrimes(TestCase):
    def test_1(self):
        l1 = [1, 2, 5]
        l2 = [1, 3, 5]
        result = [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 625, 1000, 1250, 2500, 3125, 5000, 6250, 12500, 25000]    
        self.assertEqual(get_dividers(l1, l2), result)

    def test_2(self):
        l1 = [1, 11, 5]
        l2 = [1, 1, 3]
        result = [1, 5, 11, 25, 55, 125, 275, 1375]
        self.assertEqual(get_dividers(l1, l2), result)

if __name__ == "__main__":
    main()