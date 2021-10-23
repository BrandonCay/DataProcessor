import unittest
from production.Normalizer import Normalizer
import pandas as pd

class TestNormalizedCol(unittest.TestCase):
    def __init__ (self):
        self.unnormalizedData=pd.DataFrame
        (
            {
                'Column 1':[200,-4,90,13.9,5,-90,20,300.7,30,-200,400],
                'Column 2':[20,30,23,45,19,38,25,45,34,37,12]
            }
        )

        print("TYPE OF DF: " + str(self.unnormalizedData))

        self.expectedLastNormalizedDataFromCol1= 1.000000
        self.normalizer = Normalizer(self.unnormalizedData)

    def test_normalize(self):
        column = 'Column 1'
        normalizedDf= self.normalizer.normalize(column)
        lastElementIndex = len(normalizedDf[column]) - 1
        lastElementInNormalizedDfCol1 = normalizedDf[column][lastElementIndex]
        decimalPlaces = 2

        print("test_normalize")
        
        self.assertAlmostEqual(lastElementInNormalizedDfCol1, self.expectedLastNormalizedDataFromCol1, decimalPlaces, "assertRan" )    
    def run(self):
        self.test_normalize()
