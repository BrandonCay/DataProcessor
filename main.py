import pandas as pd
from production.Normalizer import Normalizer
from data.paths import pathToCsv, pathToDataDir, pathToDataDirWithOs,pathToCsvFile_2021_11_15
from production.defaultSetupLogger import defaultSetupLogger
from production.ReplaceColNamesWithARow import ReplaceColNamesWithARow
from production.DataProcessorForData_2021_11_15 import DataProcessorForData_2021_11_15
from production.dfViewMethods import printCols

log = defaultSetupLogger(__file__)




"""
No. of Iteration: 13 gets converted to 12.5
"""


def main():
    unprocessed = pd.read_csv(pathToCsvFile_2021_11_15)
    log.debug(unprocessed.describe())
    printCols(unprocessed, unprocessed.columns)
    dataProcessor = DataProcessorForData_2021_11_15(unprocessed)
    newDf = dataProcessor.process()
    

def exportFile(processed: pd.DataFrame , nameOfFile : str) -> None:
    processed.to_csv(pathToDataDir + f"\\{nameOfFile}.csv", index=False)


"""
NOTE:
Strings at rows 0 and 33
No strings in range of [1:33] 
"""


if (__name__ == '__main__'):
    main()