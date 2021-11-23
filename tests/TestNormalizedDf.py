import unittest
from pandas.testing import assert_frame_equal
from data.pythonData import newAttrTable, normalizedNewAttrTable
from production.DataProcessorNewAttr import DataProcessorNewAttr
from production.Normalizer import Normalizer
from production.defaultSetupLogger import defaultSetupLogger
import pandas as pd 
log = defaultSetupLogger(__file__)

class TestNormalizedDf(unittest.TestCase):
    def __init__(self, ):
        self.__givendf = newAttrTable
        self.__expectedDf=self.__processExpectedData()
    
    def test_normalizeDf(self):
        log.debug(f"EXP\n {self.__expectedDf.columns}\n")
        log.debug(f"{self.__expectedDf.dtypes}")
        log.debug(f"GIV\n {self.__givendf.dtypes}\n")

        normalizedDf = self.__processGivenData()

        log.debug(f"EXP\n {self.__expectedDf.columns}\n")
        log.debug(f"{self.__expectedDf.dtypes}")
        log.debug(f"GIVEN NORM\n {normalizedDf.columns}\n")
        log.debug(f'{normalizedDf.dtypes}')
        log.debug("DIFF:")
        assert_frame_equal(normalizedDf, self.__expectedDf)

    def __processGivenData(self, endOfColumnSlice = 18, startOfColumnSlice = 2) -> pd.DataFrame :
        dp = DataProcessorNewAttr(self.__givendf)
        unprocessed = dp.process()
        processed = unprocessed.iloc[:,startOfColumnSlice:endOfColumnSlice]
        return processed
    
    def __processExpectedData(self, startOfColumnSlice = 2,endOfColumnSlice = 18) -> pd.DataFrame:
        processed = normalizedNewAttrTable.iloc[:, startOfColumnSlice :endOfColumnSlice]
        return processed
        
        

        
    
    def run(self):
        self.test_normalizeDf()
          