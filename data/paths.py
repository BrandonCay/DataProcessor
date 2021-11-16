import os
#from production.defaultSetupLogger import defaultSetupLogger
#log = defaultSetupLogger(__file__)

pathToCsv = r"C:\Users\Brandon\Documents\College\Fall2021\CS4800-CS-Seminar\researchProj\colabCode\DataProcessor\data\new attributes for DNN.csv"
pathToDataDir = r"C:\Users\Brandon\Documents\College\Fall2021\CS4800-CS-Seminar\researchProj\colabCode\DataProcessor\data"
pathToDataDirWithOs = os.getcwd() #gets cwd of __main__
fileName_2021_11_15 = "correct data for adjusted ET"
absolutePathToLog = rf'C:\Users\Brandon\Documents\College\Fall2021\CS4800-CS-Seminar\researchProj\colabCode\DataProcessor\logs'
pathToCsvFile_2021_11_15=pathToDataDir + f"\\{fileName_2021_11_15}.csv"


if(__name__ == '__main__'):
    #log.debug(pathToDataDirWithOs) doesn't exist
    print(pathToCsvFile_2021_11_15)