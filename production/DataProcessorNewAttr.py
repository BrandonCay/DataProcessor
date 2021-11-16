import pandas as pd
from production.__absDataProcessor import absDataProcessor
from production.ReplaceColNamesWithARow import ReplaceColNamesWithARow
from production.dfViewMethods import printColsList, printCols
from production.Normalizer import Normalizer
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)

class DataProcessorNewAttr(absDataProcessor):
    def __init__(self, df: pd.DataFrame):
        super().__init__(self, df)
    
    def process(self) -> pd.DataFrame:
        unprocessed = self.get_unprocessed()
        unprocessed = unprocessed.dropna(how='all', axis=1)
        unprocessed = unprocessed.dropna(how='all', axis=0)

        replacer1 = ReplaceColNamesWithARow(unprocessed)
        
        printColsList(unprocessed)

        unprocessed = replacer1.replaceColNamesWithARow()
        
        printColsList(unprocessed)

        columnToDrop = "execution time"

        unprocessed = unprocessed.drop(columnToDrop, axis = 1)
        unprocessed = unprocessed.drop(unprocessed.columns[0:2] , axis=1)
        unprocessed = unprocessed.drop(33 , axis=0)




        printColsList(unprocessed)

        printCols(unprocessed, unprocessed.columns)

        colNameToKeep = " adjusted execution time"
        for colNameToNormalize in unprocessed.columns:
            if( colNameToNormalize!= colNameToKeep):
                colToNormalize = unprocessed[colNameToNormalize]
                colToNormalize = pd.to_numeric(colToNormalize) # assumes all are numeric
                normalizer1 = Normalizer(colToNormalize)
                normalizedCol = normalizer1.normalize()
                unprocessed[colNameToNormalize] = normalizedCol

        printColsList(unprocessed)

        log.debug(unprocessed[:3])

        colNameToRemoveLeadingSpaces = colNameToKeep
        colNameAfterSpacesRemoved = colNameToRemoveLeadingSpaces.lstrip()
        unprocessed = unprocessed.rename({colNameAfterSpacesRemoved : colNameAfterSpacesRemoved})

        printColsList(unprocessed)

        return unprocessed

