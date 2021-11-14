import unittest
from pandas._testing import assert_frame_equal
import pandas as pd

class TestPandasAssertEqualGivenSelf(unittest.TestCase):
    def __init__(self):
        self.__testDataDf = pd.DataFrame({'col':[1,1,1]})  
    
    def test_compareSelfToSelf(self):
        assert_frame_equal(self.__testDataDf, self.__testDataDf)
    
    def test_compareIntSelfToFloatSelf(self):
        df = self.__testDataDf * 1.00
        assert_frame_equal(self.__testDataDf, df, check_dtype=False )
    def run(self):
        self.test_compareSelfToSelf()
        self.test_compareIntSelfToFloatSelf()

    
    

        
        
    