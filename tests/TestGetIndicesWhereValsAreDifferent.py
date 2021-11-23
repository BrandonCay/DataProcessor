import unittest
import pandas as pd
from production.ComparerOfTwoTables import ComparerOfTwoTables
from pandas.testing import assert_frame_equal
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)

class TestGetIndicesWhereValsAreDifferent(unittest.TestCase):
    def __init__(self):
        self.__givenReference = pd.DataFrame({"col1":[0,0,0], "col2":[0,0,0]})
        self.__givenComparison=pd.DataFrame({'col1':[0,0,1], 'col2':[0,1,0]})
        self.__expectedIndices={'col1':[2], 'col2':[1]}
    
    def test_comparer(self):
        c = ComparerOfTwoTables(self.__givenReference, self.__givenComparison)
        indices = c.getIndices()
        log.debug(indices)

        self.assertDictEqual(indices, self.__expectedIndices)

    
    def run(self):
        self.test_comparer()