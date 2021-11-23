import os
#from production.defaultSetupLogger import defaultSetupLogger
#log = defaultSetupLogger(__file__)

flagHome =False


pathToCsv = r"C:\Users\Brandon\Documents\College\Fall2021\CS4800-CS-Seminar\researchProj\colabCode\DataProcessor\data\new attributes for DNN.csv"
pathToDataDir = r"C:\Users\Brandon\Documents\College\Fall2021\CS4800-CS-Seminar\researchProj\colabCode\DataProcessor\data"
pathToDataDirWithOs = os.getcwd() #gets cwd of __main__
fileName_2021_11_15 = "correct data for adjusted ET"
absolutePathToLog = rf'C:\Users\Brandon\Documents\College\Fall2021\CS4800-CS-Seminar\researchProj\colabCode\DataProcessor\logs'
pathToVerifiedNormalizedCSV=None
pathToNewAttr=None

if(flagHome == False):
    pathToDataDir = r"C:\Users\brand\OneDrive\Documents\college\CS4800\code\DataProcessor\data"
    absolutePathToLog = r"C:\Users\brand\OneDrive\Documents\college\CS4800\code\DataProcessor\logs"
    pathToVerifiedNormalizedCSV=r"C:\Users\brand\OneDrive\Documents\college\CS4800\code\DataProcessor\data\correct pure normalized data.csv"
    pathToNewAttr=r"C:\Users\brand\OneDrive\Documents\college\CS4800\code\DataProcessor\data\new attributes for DNN.csv"


pathToCsvFile_2021_11_15=pathToDataDir + f"\\{fileName_2021_11_15}.csv"


if(__name__ == '__main__'):
    #log.debug(pathToDataDirWithOs) doesn't exist
    print(pathToCsvFile_2021_11_15)