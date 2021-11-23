import unittest
import pandas as pd
from production.ComparerOfTwoTables import ComparerOfTwoTables
from pandas.testing import assert_frame_equal

class TestGetIndicesWhereValsAreDifferent(unittest.TestCase):
    def __init__(self):
        self.__givenReference = pd.DataFrame({"col1":[0,0,0]})
        self.__givenComparison=pd.DataFrame({'col1':[0,0,1]})
        self.__expectedIndices=[2]
    
    def test_comparer(self):
        c = ComparerOfTwoTables(self.__givenReference, self.__givenComparison)
        indices = c.getIndices()
        self.assertEqual(indices, self.__expectedIndices)

    
    def run(self):
        self.test_comparer()