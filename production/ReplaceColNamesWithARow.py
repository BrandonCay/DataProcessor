import pandas as pd
from collections import defaultdict


class ReplaceColNamesWithARow:
    def __init__(self, df : pd.DateFrame, indexOfRowToUseForReplacement = 0):
        self.__df = df
        self.__indexOfRowToUseForReplacement = indexOfRowToUseForReplacement
    def set_indexOfRowToUseForReplacement(self, newIndex : int):
        self.__indexOfRowToUseForReplacement= newIndex
    
    def replaceColNamesWithARow(self) -> pd.DataFrame:
        newColNames = self.__get_newColNames()
        newDf = self.__get_dfAfterRowDropped()
        oldNamesToNewNames = self.__makeDictOfOldColNamesToNewColNames(newColNames)
        newDf = newDf.rename(columns=oldNamesToNewNames)
        return newDf
        
        
    
    def __get_newColNames(self) -> list:
        return self.__df.iloc[[self.__indexOfRowToUseForReplacement]]
    
    def __get_dfAfterRowDropped(self) -> pd.DataFrame:
        return self.__df.drop(self.__indexOfRowToUseForReplacement)

    def __makeDictOfOldColNamesToNewColNames(self, newColNames : list) -> dict:
        oldColNames = list(self.__df.columns)
        oldNamesToNewNames = defaultdict(lambda : "not a key")
        lenOfOldColNames = len(oldColNames)
        
        for indexOfOldColName in lenOfOldColNames:
            oldColName = oldColNames[indexOfOldColName]
            newColName = newColNames[indexOfOldColName]
            oldNamesToNewNames[oldColName] = newColName

        return oldNamesToNewNames
        
        

        
        
        


