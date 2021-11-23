import pandas as pd
import numpy as np
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)

class ComparerOfTwoTables:
    def __init__(self, referenceData : pd.DataFrame, comparisonData: pd.DataFrame):
        self.__referenceData = referenceData
        self.__comparisonData = comparisonData
        self.__absoluteTolerance = 1e-3

    def getIndices(self) -> list:
        absoluteDifference = (self.__referenceData - self.__comparisonData).abs()
        indices = absoluteDifference[absoluteDifference > self.__absoluteTolerance]
        log.debug(indices)
        return list(indices)
    
    