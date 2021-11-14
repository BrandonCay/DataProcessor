import logging
import os

def setup_logger(logger_name, log_file, level=logging.DEBUG):
    log_file = os.path.basename(log_file)
    absolutePathOfFile = rf'C:\Users\Brandon\Documents\College\Fall2021\CS4800-CS-Seminar\researchProj\colabCode\normalizeData\logs\{log_file}'
    print("ABS: " + absolutePathOfFile)
    log_file = absolutePathOfFile
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(lineno)d : %(asctime)s : %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)    
