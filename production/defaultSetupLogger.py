from production.setup_logger import setup_logger
import logging 

def defaultSetupLogger(currFile) -> logging.Logger:
    currFileName = str(currFile)
    setup_logger(currFileName, currFileName + ".log")
    return logging.getLogger(currFileName)
