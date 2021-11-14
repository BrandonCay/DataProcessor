import pandas as pd
from production.Normalizer import Normalizer


df_min_max_scaled = pd.read_excel('new attributes for DNN2.xlsx', index_col=[0])
columnsList = df_min_max_scaled.columns

"""
NOTE: 
No. of Iteration: 13 gets converted to 12.5
"""
def main():
    i=-1
    for colName in columnsList:            
        i+=1
        if(i==0 or i>=20):
            continue
        colList = getColAsList(colName,1,34)
        normalizerObj = Normalizer(colList)
        normalizedList = normalizerObj.normalize()
        copyNormalizedDataToDF(normalizedList, colName, 1, 34)
    
    df_min_max_scaled.to_excel('normalization of new attributes for DNN2.xlsx')



def getColAsList(colName, startIndex = 0, endIndex = 1):
    sCol = df_min_max_scaled[colName]
    return sCol[startIndex:endIndex].to_list()

        
def copyNormalizedDataToDF(listOfNormalizedData, colName, startIndexOfDf, endIndexOfDf):
    normalizedIndex = 0
    for index in range(startIndexOfDf, endIndexOfDf):
        df_min_max_scaled[colName][index] = listOfNormalizedData[normalizedIndex]
        normalizedIndex += 1 

        
    

def printCols():
     for i in columnsList:
        print(df_min_max_scaled[i])


def printColName():
    print(df_min_max_scaled.iloc[1])

def findStringInDf():
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



"""
NOTE:
Strings at rows 0 and 33
No strings in range of [1:33] 
"""


if (__name__ == '__main__'):
    main()