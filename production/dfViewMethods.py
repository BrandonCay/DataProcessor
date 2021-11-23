from production.defaultSetupLogger import defaultSetupLogger
import pandas as pd
from logging import Logger

log = defaultSetupLogger(__file__)    



def printColsList(df : pd.DataFrame, log: Logger):
    columnsList = df.columns
    log.debug(columnsList)

    
def getColAsList(df_min_max_scaled : pd.DataFrame, colName : str, startIndex = 0, endIndex = 1) -> list:
    sCol = df_min_max_scaled[colName]
    return sCol[startIndex:endIndex].to_list()

        
def copyNormalizedDataToDF(df_min_max_scaled : pd.DataFrame, listOfNormalizedData, colName, startIndexOfDf, endIndexOfDf):
    normalizedIndex = 0
    for index in range(startIndexOfDf, endIndexOfDf):
        df_min_max_scaled[colName][index] = listOfNormalizedData[normalizedIndex]
        normalizedIndex += 1 

        
    

def printCols(df:pd.DataFrame,columnsList :list, log :log):
    for i in columnsList:
        log.debug("\n")
        log.debug(df[i] )


def printColName(df_min_max_scaled : pd.DataFrame):
    print(df_min_max_scaled.iloc[1])

def findStringInDf(df_min_max_scaled : pd.DataFrame, columnsList : list):
    colCnt = 0
    for col in columnsList:
        print("COL NUM: " + str(colCnt))
        col = df_min_max_scaled[col]
        col = col.to_list()
        row = 0
        for el in col:
            if isinstance(el, str):
                print("FOUND:  "  + str(row))
                print(el)
            row = row + 1
        colCnt = colCnt + 1

