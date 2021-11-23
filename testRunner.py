from tests.TestNormalizedCol import  TestNormalizedCol
from tests.TestPandasAssertEqualGivenSelf import TestPandasAssertEqualGivenSelf
from tests.TestReplaceColumnNameGivenWrongColumnNames import TestReplaceColumnNameGivenWrongColumnNames
from tests.TestNormalizedCol import TestNormalizedCol
from tests.TestGetNormalizedData import TestGetNormalizedData
import pandas as pd
from production.defaultSetupLogger import defaultSetupLogger
from tests.TestNormalizedDf import TestNormalizedDf
from tests.TestGetNormalizedET import TestGetNormalizedET
from tests.TestGetIndicesWhereValsAreDifferent import TestGetIndicesWhereValsAreDifferent
log = defaultSetupLogger(__file__)

#test runner replaces the built-in test feature because I'm not too familiar with it as of 2021/11/14 
def allTests():
    tncObj = TestNormalizedCol()
    tncObj.run()

def runOne():
    tObj = TestGetIndicesWhereValsAreDifferent()
    tObj.run()


if __name__ == '__main__':
    runOne()
    