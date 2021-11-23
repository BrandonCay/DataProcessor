from data.paths import pathToNewAttr
from data.paths import pathToVerifiedNormalizedCSV
import pandas as pd
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)

newAttrTable = pd.DataFrame(pd.read_csv(pathToNewAttr))
normalizedNewAttrTable = pd.DataFrame((pd.read_csv(pathToVerifiedNormalizedCSV)))

log.debug(newAttrTable.describe())