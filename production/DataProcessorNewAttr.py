import pandas as pd
from production.__absDataProcessor import absDataProcessor
from production.ReplaceColNamesWithARow import ReplaceColNamesWithARow
from production.dfViewMethods import printColsList, printCols
from production.Normalizer import Normalizer
from production.defaultSetupLogger import defaultSetupLogger
from data.pythonData import newAttrTable
log = defaultSetupLogger(__file__)

class DataProcessorNewAttr(absDataProcessor):
    def __init__(self, df = newAttrTable) -> None:
        super().__init__(df)
        self.__colsToRename = dict({" adjusted execution time": "adjusted execution time"})
        self.__colNameToKeep = str(" adjusted execution time")
        self.__colNameToDrop = "execution time"


    def process(self, steps = 5) -> pd.DataFrame:
        unprocessed = self.get_unprocessed()
        printCols(unprocessed,unprocessed.columns, log)

        unprocessed = self.__dropNaSections(unprocessed)

        replacer1 = ReplaceColNamesWithARow(unprocessed)

        unprocessed = replacer1.replaceColNamesWithARow()
        
        unprocessed  = self.__dropSections(unprocessed)#td: elim pass

        unprocessed = self.__normalize(unprocessed)

        log.debug(unprocessed)

        unprocessed = self.__renameCols(unprocessed)


        if(steps <= 5):
            unprocessed = self.__processToETformat(unprocessed)
        
        processed = unprocessed

        return processed

    def __renameCols(self, unprocessed : pd.DataFrame) -> pd.DataFrame:
        unprocessed = unprocessed.rename(self.__colsToRename)
        return unprocessed
        

    def __dropSections(self, unprocessed: pd.DataFrame) -> pd.DataFrame:
        unprocessed = unprocessed.drop(self.__colNameToDrop, axis = 1)
        unprocessed = unprocessed.drop(unprocessed.columns[0:2] , axis=1)
        unprocessed = unprocessed.drop(33 , axis=0)
        return unprocessed

    def __dropNaSections(self, unprocessed: pd.DataFrame) -> pd.DataFrame:
        unprocessed = unprocessed.dropna(how='all', axis=1)
        unprocessed = unprocessed.dropna(how='all', axis=0)
        return unprocessed

    def __normalize(self, unprocessed : pd.DataFrame ) -> pd.DataFrame:
        for colNameToNormalize in unprocessed.columns:
            if( colNameToNormalize!= self.__colNameToKeep):
                colToNormalize = unprocessed[colNameToNormalize]
                colToNormalize = pd.to_numeric(colToNormalize) # assumes all are numeric
                normalizer1 = Normalizer(colToNormalize)
                normalizedCol = normalizer1.normalize()
                unprocessed[colNameToNormalize] = normalizedCol
        return unprocessed

    def __processToETformat(self, unprocessed: pd.DataFrame):
        oldColNamesToNewColNames = {" adjusted execution time": "adjusted execution time"
        ,"Repeating times":"repeating time"}
        processed = unprocessed.rename(columns  = oldColNamesToNewColNames)
        return processed

    



        

        
        
        
        

