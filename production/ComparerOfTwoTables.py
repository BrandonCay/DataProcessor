import pandas as pd
import numpy as np
from pandas.core.tools import numeric
from production.defaultSetupLogger import defaultSetupLogger
import math
from pandas.api.types import is_numeric_dtype

log = defaultSetupLogger(__file__)

class ComparerOfTwoTables:
    def __init__(self, referenceData : pd.DataFrame, comparisonData: pd.DataFrame):
        self.__referenceData = referenceData
        self.__comparisonData = comparisonData
        self.__absoluteTolerance = 1e-3

    def getIndices(self) -> list:        
        colNameToIndices = {}
        for colName in self.__referenceData.columns:
            if(self.__isNumeric(self.__referenceData[colName]) and self.__isNumeric(self.__comparisonData[colName])):
                absoluteDifference = pd.Series(self.__referenceData[colName] - self.__comparisonData[colName]).abs()
                indices = pd.Series(absoluteDifference.index[absoluteDifference > self.__absoluteTolerance])
                indices = indices.to_list()
                colNameToIndices[colName] = indices
            else:
                colNameToIndices[colName] = [-1]

        return colNameToIndices

    def set_comparisonData(self):
        pass
    
    def __pickIndex(self, e1, e2 ):
        return math.abs( (e1-e2) > self.__absoluteTolerance )

    def __pickSeries(self, s1: pd.Series , s2) -> pd.Series:
        return s1
    
    def __isNumeric(self, s:pd.Series) -> bool:
        return is_numeric_dtype(s)
            
        
    
    