from tests.TestNormalizedCol import  TestNormalizedCol
from tests.TestPandasAssertEqualGivenSelf import TestPandasAssertEqualGivenSelf
import pandas as pd

#test runner replaces the built-in test feature because I'm not too familiar with it as of 2021/11/14 
def allTests():
    tncObj = TestNormalizedCol()
    tncObj.run()

def runOne():
    tObj = TestPandasAssertEqualGivenSelf()
    tObj.run()
    


if __name__ == '__main__':
    runOne()
    