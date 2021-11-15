import unittest
from pandas.testing import assert_frame_equal
import pandas as pd
from production.ReplaceColNamesWithARow import ReplaceColNamesWithARow
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)

class TestReplaceColumnNameGivenWrongColumnNames(unittest.TestCase):
    def __init__(self):
        self.__expectedDf= pd.DataFrame({'col1':[1,1,1]})
        self.__givenDf= pd.DataFrame({'Unnamed: 0':['col1',1,1,1]})

    def test_replaceHeaders(self):

        log.debug("CHECK D:\n" + self.__givenDf.dtypes.to_string())

        rcnObj = ReplaceColNamesWithARow(self.__givenDf, 0)
        newDf = rcnObj.replaceColNamesWithARow()

        log.debug("CHECK D:\n" + newDf.dtypes.to_string())
        log.debug("NEW DF \n" + newDf.to_string())
        log.debug ("EXPECTED DF\n" + self.__expectedDf.to_string())
        log.debug("CHECK D:\n" + newDf.dtypes.to_string())

        assert_frame_equal(newDf, self.__expectedDf)

    def run(self):
        self.test_replaceHeaders()