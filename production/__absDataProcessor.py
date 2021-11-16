import pandas as pd

class absDataProcessor():
    def __init__ (self, unprocessed : pd.DataFrame) -> None:
        self.__unprocessed = unprocessed

    def get_unprocessed(self) -> pd.DataFrame:
        return self.__unprocessed
        
    def process(self) -> pd.DataFrame:
        return pd.DataFrame()
