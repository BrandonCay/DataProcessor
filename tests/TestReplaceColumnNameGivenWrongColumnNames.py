import unittest
from pandas.testing import assert_frame_equal
import pandas as pd
from production.ReplaceColNamesWithARow import ReplaceColNamesWithARow

class TestReplaceColumnNameGivenWrongColumnNames(unittest.TestCase):
    def __init__(self):
        self.__expectedDf= pd.DataFrame({'col1':[1,1,1]})
        self.__givenDf= pd.DataFrame({'Unnamed: 0':['col1',1,1,1]})

    def test_replaceHeaders(self):
        rcnObj = ReplaceColNamesWithARow(self.__givenDf)
        newDf = rcnObj.replaceColNamesWithARow()

        print(newDf, self.__expectedDf)

        assert_frame_equal(newDf, self.__expectedDf)

    def run(self):
        self.test_replaceHeaders()