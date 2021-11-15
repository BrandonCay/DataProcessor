import pandas as pd
from collections import defaultdict
import logging
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)


class ReplaceColNamesWithARow:
    def __init__(self, df : pd.DataFrame, indexOfRowToUseForReplacement = 0):
        self.__df = pd.DataFrame(df)
        self.__indexOfRowToUseForReplacement = indexOfRowToUseForReplacement

    def set_indexOfRowToUseForReplacement(self, newIndex : int):
        self.__indexOfRowToUseForReplacement= newIndex
    
    def replaceColNamesWithARow(self) -> pd.DataFrame:

        log.debug("CHECK TYPE OF DF:\n" + self.__df.dtypes.to_string())

        newColNames = self.__get_newColNames()

        log.debug("CHECK TYPE OF DF:\n" + self.__df.dtypes.to_string())
        
        log.debug("NEW COLUMN NAMES: "  + str(newColNames))


        newDf = self.__get_dfAfterRowDropped()

        log.debug("CHECK TYPE OF DF:\n" + newDf.to_string())

        oldNamesToNewNames = self.__makeDictOfOldColNamesToNewColNames(newColNames)
        newDf = self.__resetIndex(newDf)

        log.debug("CHECK TYPE OF DF:\n" + newDf.to_string())

        newDf = newDf.rename(columns=oldNamesToNewNames)

        log.debug("CHECK TYPE OF DF:\n" + newDf.dtypes.to_string())
        log.debug(oldNamesToNewNames)

        newDf = newDf.infer_objects()
        
        log.debug("CHECK TYPE OF DF:\n" + newDf.dtypes.to_string())
        log.debug("CHECK DF AFTER infer:\n" +  newDf.to_string())

        return newDf
        
    
    def __get_newColNames(self) -> list:
        names = pd.Series(self.__df.iloc[self.__indexOfRowToUseForReplacement, :])
        log.debug("Names after df slice:\n" + names.to_string())
        names = names.iloc[:]
        log.debug("Names after s slice:\n" + names.to_string())
        
        return list(names)
    
    def __get_dfAfterRowDropped(self) -> pd.DataFrame:
        return self.__df.drop(self.__indexOfRowToUseForReplacement)

    def __makeDictOfOldColNamesToNewColNames(self, newColNames : list) -> dict:
        oldColNames = list(self.__df.columns)
        oldNamesToNewNames = defaultdict(lambda : "not a key")

        log.debug("OLDNAMES: " + str(oldColNames) )
        log.debug("NEW NAMES: " + str(newColNames))

        lenOfOldColNames = len(oldColNames)
        
        for indexOfOldColName in range(lenOfOldColNames):
            oldColName = oldColNames[indexOfOldColName]
            newColName = newColNames[indexOfOldColName]
            oldNamesToNewNames[oldColName] = newColName

        return oldNamesToNewNames
    
    def __resetIndex(self, newDf : pd.DataFrame) -> pd.DataFrame:
        return newDf.reset_index(drop = True)
        
        
        

        
        
        


