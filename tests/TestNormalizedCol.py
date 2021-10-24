import unittest
from production.Normalizer import Normalizer
import pandas as pd
"""
                'Column 1':[200,-4,90,13.9,5,-90,20,300.7,30,-200,400],
                'Column 2':[20,30,23,45,19,38,25,45,34,37,12]

"""
class TestNormalizedCol(unittest.TestCase):
    def __init__ (self):
        listForSeries= [200,-4,90,13.9,5,-90,20,300.7,30,-200,400]
         
        self.unnormalizedData=pd.Series(listForSeries)
       
        self.expectedLastNormalizedDataFromCol1= 1.000000
        self.normalizer = Normalizer(listForSeries)
    def test_normalize(self):
        
        normalizedS= self.normalizer.normalize()
        lastElementIndex = len(normalizedS) - 1
        lastElementInNormalizedSCol1 = normalizedS[lastElementIndex]
        decimalPlaces = 2
        
        self.assertAlmostEqual(lastElementInNormalizedSCol1, self.expectedLastNormalizedDataFromCol1, decimalPlaces, "NOT EQUAL" )


    def run(self):
        self.test_normalize()
