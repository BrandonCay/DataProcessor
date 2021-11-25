import pandas as pd
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)
import numpy as np

class UnionOfDataFormatter:
    def __init__ (self, dataFramesToFormat : list, dataFrameNames : list) -> None:
        self.__dataframes= dataFramesToFormat
        self.__names = dataFrameNames
    
    def getDataAtLocations(self, colNameToIndices : dict) -> pd.DataFrame:
        #self.__setupFormattedData(["indices" , "colName"])

        colNamesOfFormattedData = ["colName" , "indices"] + self.__names 
        valuesToAppendToFormattedData = []
        #indiciesOfFormattedColData = self.__makeIndexNameToIndexNumber(colNames)

        for colName in colNameToIndices.keys():

            indices = colNameToIndices[colName]
            indexOfColOfFormattedData=0 
            for index in indices:
                valuesToAppendToFormattedData.append([]) #create list for row
                valuesToAppendToFormattedData[indexOfColOfFormattedData].append(colName)
                valuesToAppendToFormattedData[indexOfColOfFormattedData].append(index)
                for df in self.__dataframes:
                    dataAtLocation = None
                    if colName in df:
                        dataAtLocation = df[colName][index]
                    
                    valuesToAppendToFormattedData[indexOfColOfFormattedData].append(dataAtLocation)

                indexOfColOfFormattedData+=1

                log.debug(valuesToAppendToFormattedData)

        log.debug( valuesToAppendToFormattedData)
        log.debug( colNamesOfFormattedData )   

        formattedData = pd.DataFrame(valuesToAppendToFormattedData , columns = colNamesOfFormattedData )
        return formattedData
    
    def __makeIndexNameToIndexNumber(self, keyValues : list , indexToStopAt : int) -> dict:
        res = dict()
        for key in keyValues:
            for index in range(0, indexToStopAt):
                res[key] = index 
                
        return res

    def __initValuesToAppendToFormattedData(self, colsOfFormattedData : list()) ->list(list()):
        base  =  []
        for col in colsOfFormattedData:
            base.append([])
        
        return base 
    
    def __initFormattedData(self, otherColNames = []) -> pd.DataFrame:
        formattedColumns = self.__names + otherColNames
        return pd.DataFrame(columns=formattedColumns) 
