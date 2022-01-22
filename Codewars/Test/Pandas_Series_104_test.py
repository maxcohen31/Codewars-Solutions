import pandas as pd
import unittest
from Pandas_Series_104_Flatten_rows_from_DataFrame_solution import flatten
from pandas.testing import assert_frame_equal

class Flatten(unittest.TestCase): 
    def test(self):
        dataframe = pd.DataFrame(data=[[[1, 2],5], [['a', 'b', 'c'], 6], [77, 3]], columns=list('AB'))
        result = pd.DataFrame({'A': [1, 2, 'a', 'b', 'c', 77], 'B': [5, 5, 6, 6, 6, 3]})
        assert_frame_equal(flatten(dataframe, 'A'), result)
        
if __name__ == '__main__':
    unittest.main()