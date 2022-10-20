from Mean_Square_Error_5_kyu import solution
import unittest


class MeanSquareError(unittest.TestCase):
    def test_1(self):
        input_ = [
            (([1, 2, 3], [4, 5, 6]), 9),
            (([10, 20, 10, 2], [10, 25, 5, -2]), 16.5),
            (([-3, 4, 5, 919, 666, -69], [12, 3, 55, 911, 555, 44]), 4646.666666666667)
        ]

        for (i, j), z in input_:
            testing = self.assertEqual(solution(i, j), z)
        return testing
        

if __name__ == '__main__':
    unittest.main()
