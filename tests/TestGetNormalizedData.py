import unittest 
import pandas as pd
from production.Normalizer import Normalizer
from pandas.testing import assert_series_equal
from data.pythonData import newAttrTable
from data.pythonData import normalizedNewAttrTable
from production.DataProcessorNewAttr import DataProcessorNewAttr
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)
import math

#source of data = https://datagy.io/pandas-normalize-column/
class TestGetNormalizedData(unittest.TestCase):
    def __init__(self):
        dp =DataProcessorNewAttr(newAttrTable)
        dp = dp.process()

        sampleColName = "Number of statements"
        s = dp[sampleColName]
        self.__givenSeries=pd.Series(s)
        self.__expectedSeries = pd.Series(normalizedNewAttrTable[sampleColName])
        
    def test_normalizer(self):
        unnormalizedCol = pd.Series(self.__givenSeries)
        normalizer1 = Normalizer(unnormalizedCol)
        normalizedCol = normalizer1.normalize()
        
        log.debug("Expected")
        log.debug(self.__expectedSeries)

        normalizedCol = self.__round(normalizedCol, 9)
        
        log.debug("Normalized and Rounded by 9 deci")
        log.debug(normalizedCol)


        assert_series_equal(normalizedCol, self.__expectedSeries, atol = 1e-2, rtol=0)

    def __truncate(self, normalizedCol : pd.Series, decimalPlaces : int):
        numToUseForTruncate = 10 ** decimalPlaces
        trunc = lambda x: math.trunc(numToUseForTruncate * x) / numToUseForTruncate
        return normalizedCol.apply(trunc)
    
    def __round(self, normalizedCol : pd.Series, decimalPlaces : int):
        return normalizedCol.round(decimalPlaces)

        

         
    

        
        
        

    def run(self):
        self.test_normalizer()
