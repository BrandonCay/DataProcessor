from data.pythonData import correctPure, newAttrTable
from data.proccessedPythonData import processed_2021_11_15, processed_New_Attr
from production.defaultSetupLogger import defaultSetupLogger
from production.UnionOfDataFormatter import UnionOfDataFormatter
from production.ComparerOfTwoTables import ComparerOfTwoTables

import pandas as pd 

log = defaultSetupLogger(__file__)



def main():
    dataframes = [correctPure, processed_New_Attr, processed_2021_11_15, ]
    ct = ComparerOfTwoTables(processed_New_Attr, processed_2021_11_15)
    indices = ct.getIndices()
    dfNames = ["correct pure normalized (github)", "processed_New_Attr (normalized)" , "processed_2021_11_15 (ET) (normalized)"]
    formatter = UnionOfDataFormatter(dataframes, dfNames)
    df = formatter.getDataAtLocations(indices)
    df.to_csv("data/differentVals.csv", index=False)


    


if(__name__ == '__main__'):
    main()

    