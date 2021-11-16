import pandas as pd

class absDataProcessor():
    def __init__ (self, unprocessed : pd.DataFrame) -> None:
        self.__unprocessed = unprocessed

    def process(self) -> pd.DataFrame:
        return pd.DataFrame()
