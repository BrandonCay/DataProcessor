import pandas as pd
import unittest
from pandas.testing import assert_frame_equal
from production.UnionOfDataFormatter import UnionOfDataFormatter
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)

class TestFormattedOfUnionData(unittest.TestCase):
    def __init__(self):
        self.__givenDfs = [pd.DataFrame({ 'c1': [0,0,0] }) , pd.DataFrame({'c1': [1,1,1]}) ]
        self.__expectedDf = pd.DataFrame({'colName':['c1', 'c1','c1'], 'indices' : [0,1,2] , 'a' : [0,0,0], 'b': [1,1,1] })
    
    def test_getFormattedData(self):
        dfNames = ['a','b']
        formatter = UnionOfDataFormatter(self.__givenDfs , dfNames)
        indices = {'c1': [0,1,2]}
        resDf = formatter.getDataAtLocations(indices)
        log.debug(resDf)
        log.debug(self.__expectedDf)
        assert_frame_equal(self.__expectedDf, resDf)
    
    def run(self):
        self.test_getFormattedData()
        
