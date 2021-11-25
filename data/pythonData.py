from data.paths import pathToNewAttr, pathToETcsv, pathToCorrectPure
from data.paths import pathToVerifiedNormalizedCSV
import pandas as pd
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)

newAttrTable = pd.DataFrame(pd.read_csv(pathToNewAttr))
normalizedNewAttrTable = pd.DataFrame((pd.read_csv(pathToVerifiedNormalizedCSV)))
tableET = pd.DataFrame(pd.read_csv(pathToETcsv))
correctPure = pd.DataFrame(pd.read_csv(pathToCorrectPure))