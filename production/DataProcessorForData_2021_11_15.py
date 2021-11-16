from numpy import product
from production.__absDataProcessor import absDataProcessor
import pandas as pd
from production.Normalizer import Normalizer
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)

class DataProcessorForData_2021_11_15(absDataProcessor):
    def __init__(self, unprocessed : pd.DataFrame) -> None:
        super().__init__(unprocessed)
    
    def process(self) -> pd.DataFrame:
        unprocessed = self.get_unprocessed()
        
        colToNormalize = "repeating time"

        log.debug(unprocessed[colToNormalize])

        unprocessed = self.__normalize(unprocessed)

        log.debug(unprocessed[colToNormalize])

        log.debug("BEFORE SPELLC:\n" + str(unprocessed.columns))

        unprocessed = self.__spellCorrect(unprocessed)

        log.debug(unprocessed.columns)

        processed = self.__dropUnnecessaryCols(unprocessed)  

        log.debug(processed[colToNormalize])

        

        return processed
    
    def __normalize(self, unprocessed: pd.DataFrame) -> pd.DataFrame:
        colNameToNormalize = "repeating time"
        columnSeriesToNormalize = unprocessed[colNameToNormalize]
        normalizer1  = Normalizer(columnSeriesToNormalize)
        normalizedCol = normalizer1.normalize()
        unprocessed[colNameToNormalize] = normalizedCol
        return unprocessed
    
    def __spellCorrect(self,unprocessed: pd.DataFrame) -> pd.DataFrame:
        colNameToCaseAndSpellCorrect = "Ajusted execution time"
        colNameAfterCorrection = "adjusted execution time"
        unprocessed = unprocessed.rename(columns = {colNameToCaseAndSpellCorrect : colNameAfterCorrection})
        return unprocessed
    
    def __dropUnnecessaryCols(self,unprocessed: pd.DataFrame) -> pd.DataFrame:
        unnecessaryCols = ["Unnamed: 0", "execution time", "7/17/2021"] 
        return unprocessed.drop(unnecessaryCols, axis = 1)

