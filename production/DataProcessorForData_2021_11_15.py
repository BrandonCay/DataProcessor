from production.__absDataProcessor import absDataProcessor
import pandas as pd

class DataProcessorForData_2021_11_15(absDataProcessor):
    def __init__(self, unprocessed : pd.DataFrame) -> None:
        super().__init__(unprocessed)
    
    def process(self) -> pd.DataFrame :
        return pd.DataFrame()