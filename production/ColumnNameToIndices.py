import pandas as pd

class ColumnNameToIndices:
    def __init__ (self, colNameToIndices : dict):
        self.__colNameToIndices = colNameToIndices

    def indexInto(self, df : pd.DataFrame) -> dict:
        colNameToVals = {}
        for columnName in df.columns:
            vals = list([])
            
            if(columnName in self.__colNameToIndices and self.__notInvalidCol(columnName)):    
                indices = self.__colNameToIndices[columnName]
                
                for index in indices:
                    vals.append(df[columnName][index])
                
                colNameToVals[columnName] = vals
        
        return colNameToVals

    def __notInvalidCol(self, columnName : str) -> bool:
        return  (-1 not in self.__colNameToIndices[columnName])
        