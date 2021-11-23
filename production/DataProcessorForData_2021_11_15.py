from numpy import product
from production.__absDataProcessor import absDataProcessor
import pandas as pd
from production.Normalizer import Normalizer
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)

class DataProcessorForData_2021_11_15(absDataProcessor):
    def __init__(self, unprocessed : pd.DataFrame) -> None:
        super().__init__(unprocessed)


    def process_2021_11_16(self) -> pd.DataFrame:
        unprocessed = self.get_unprocessed()

        unprocessed = self.__operation_2021_11_16(unprocessed)
        unprocessed = self.__spellCorrect(unprocessed)
        unprocessed = self.__dropUnnecessaryCols(unprocessed)

        processed = unprocessed

        return processed

    def process(self) -> pd.DataFrame:
        unprocessed = self.get_unprocessed()
        log.debug(unprocessed.columns)
        
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
    
    def __operation_2021_11_16(self, unprocessed: pd.DataFrame) -> pd.DataFrame:
        colNameToOperateOn="repeating time"
        colSeriesToOperateOn = unprocessed[colNameToOperateOn]
        maxOfCol = colSeriesToOperateOn.max()
        unprocessed[colNameToOperateOn] = colSeriesToOperateOn/maxOfCol
        return unprocessed
        

    def __spellCorrect(self,unprocessed: pd.DataFrame) -> pd.DataFrame:
        colNameToCaseAndSpellCorrect = "Ajusted execution time"
        colNameAfterCorrection = "adjusted execution time"
        unprocessed = unprocessed.rename(columns = {colNameToCaseAndSpellCorrect : colNameAfterCorrection})
        return unprocessed
    
    def __dropUnnecessaryCols(self,unprocessed: pd.DataFrame) -> pd.DataFrame:
        unnecessaryCols = ["Unnamed: 0", "execution time", "7/17/2021"] 
        return unprocessed.drop(unnecessaryCols, axis = 1)

