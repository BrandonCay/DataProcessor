import logging
import os
from data.paths import absolutePathToLog

def setup_logger(logger_name, log_file, level=logging.DEBUG):
    logging.StreamHandler(stream=None)
    log_file = os.path.basename(log_file)
    absolutePathOfFile = rf'{absolutePathToLog}\{log_file}'
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
