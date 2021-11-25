import os

projectDir = os.getcwd()

def makePathsToFilesInProject(path, projectDir = projectDir)->str:
    return os.path.abspath(os.path.join(projectDir,path))

def makePathsToFilesInDataDir(fileName: str) -> str:
    path=f"data/{fileName}"
    return makePathsToFilesInProject(path)

absolutePathToLog = makePathsToFilesInProject("logs")

pathToCsv = makePathsToFilesInDataDir("new attributes for DNN.csv")
pathToCsvFile_2021_11_15 = makePathsToFilesInDataDir("correct data for adjusted ET")
pathToVerifiedNormalizedCSV=makePathsToFilesInDataDir("correct pure normalized data.csv")
pathToNewAttr=makePathsToFilesInDataDir("new attributes for DNN.csv")
pathToETcsv = makePathsToFilesInDataDir("correct data for adjusted ET.csv")


if(__name__ == '__main__'):
    #log.debug(pathToDataDirWithOs) doesn't exist
    print(pathToCsvFile_2021_11_15)