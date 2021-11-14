from tests.TestNormalizedCol import  TestNormalizedCol
from tests.TestPandasAssertEqualGivenSelf import TestPandasAssertEqualGivenSelf
from tests.TestReplaceColumnNameGivenWrongColumnNames import TestReplaceColumnNameGivenWrongColumnNames
import pandas as pd
import logging, sys
logging.basicConfig(filename=str(__file__)+".log", level=logging.DEBUG)


#test runner replaces the built-in test feature because I'm not too familiar with it as of 2021/11/14 
def allTests():
    tncObj = TestNormalizedCol()
    tncObj.run()

def runOne():
    tObj = TestReplaceColumnNameGivenWrongColumnNames()
    tObj.run()
    


if __name__ == '__main__':
    runOne()
    