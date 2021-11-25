import pandas as pd
from pandas.core.frame import DataFrame
from production.DataProcessorNewAttr import DataProcessorNewAttr
from production.Normalizer import Normalizer
from data.paths import pathToCsv, makePathsToFilesInDataDir,pathToCsvFile_2021_11_15
from production.defaultSetupLogger import defaultSetupLogger
from production.ReplaceColNamesWithARow import ReplaceColNamesWithARow
from production.DataProcessorForData_2021_11_15 import DataProcessorForData_2021_11_15
from production.dfViewMethods import printCols
from production.ComparerOfTwoTables import ComparerOfTwoTables
from data.pythonData import tableET, newAttrTable
from production.ColumnNameToIndices import ColumnNameToIndices


log = defaultSetupLogger(__file__)




"""
No. of Iteration: 13 gets converted to 12.5
"""


def main():
    dp = DataProcessorForData_2021_11_15()
    processed_2021_11_15 = dp.process()

    dp = DataProcessorNewAttr(newAttrTable)
    processed_New_Attr = dp.process()
    
    ct = makeComparer(processed_2021_11_15, processed_New_Attr)

    indices = getIndices(ct)

    vals = getValues(processed_2021_11_15, indices)
    
    log.debug(f"\n{indices}")
    log.debug(f"\n{vals}")


def makeComparer(df1, df2):
    ct = ComparerOfTwoTables(df1, df2)
    return ct
    


def getIndices(ct : ComparerOfTwoTables):
    return ct.getIndices()

def getValues(df1 : pd.DataFrame, indices : list):
    cToi = ColumnNameToIndices(indices)
    vals = cToi.indexInto(df1)
    return vals

             
        
                

        
        
        
    
def formatDifferentData():
    


    


def process_2021_11_15():
    unprocessed = pd.read_csv(pathToCsvFile_2021_11_15)
    dataProcessor = DataProcessorForData_2021_11_15(unprocessed)
    processed = dataProcessor.process_2021_11_16()
    printCols(processed, processed.columns)
    nameOfFile = "2021_11_16_processedData"
    exportFile(processed, nameOfFile)

    
    

def exportFile(processed: pd.DataFrame , nameOfFile : str) -> None:
    processed.to_csv(makePathsToFilesInDataDir(f"\\{nameOfFile}.csv"), index=False)


"""
NOTE:
Strings at rows 0 and 33
No strings in range of [1:33] 
"""


if (__name__ == '__main__'):
    main()