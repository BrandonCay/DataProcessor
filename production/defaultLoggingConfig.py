import logging,sys
def defaultLoggingConfig(nameOfCurrentFile: str) -> any:
    logging.basicConfig(filename=nameOfCurrentFile+".log", level=logging.DEBUG, filemode='w')
    return logging

