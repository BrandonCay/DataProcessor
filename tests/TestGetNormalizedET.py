import unittest
from pandas.testing import assert_frame_equal
from data.pythonData import newAttrTable, tableET
from production.DataProcessorNewAttr import DataProcessorNewAttr
from production.DataProcessorForData_2021_11_15 import DataProcessorForData_2021_11_15
from production.Normalizer import Normalizer
from production.defaultSetupLogger import defaultSetupLogger
import pandas as pd 
log = defaultSetupLogger(__file__)

class TestGetNormalizedET(unittest.TestCase):
    def __init__ (self):
        self.__givenData = newAttrTable
        self.__expectedData = tableET
        self.__expectedData = self.__processExpectedData()
        self.__oldColNamesToNewColNames = {" adjusted execution time": "adjusted execution time"
        ,"Repeating times":"repeating time"}
    
    def test_normalize(self) -> None: 
        processedData = self.__processGivenData()
        assert_frame_equal(processedData, self.__expectedData)
        

    def __processGivenData(self) -> pd.DataFrame:
        dp = DataProcessorNewAttr(self.__givenData)
        df = dp.process()
        df = df.rename(columns = self.__oldColNamesToNewColNames )
        return df
    
    def run(self):
        self.test_normalize()

    def __processExpectedData(self) -> pd.DataFrame:
        dp = DataProcessorForData_2021_11_15(self.__expectedData)
        df = dp.process()
        return df

        
