import pandas as pd
from pandas.api.types import is_numeric_dtype


class Normalizer:
    def __init__(self, columnData = pd.Series()):
        self.__decimalPlaces = 15
        self.__sUnnormalized = columnData


    def normalize(self) -> pd.Series:
        s_min_max_scaled = self.__sUnnormalized
        s_min_max_scaled = (s_min_max_scaled - s_min_max_scaled.min()) / (s_min_max_scaled.max() - s_min_max_scaled.min())
        return s_min_max_scaled.round(self.__decimalPlaces)


    def set_sUnnormalized(self, s):
        try:
            if not isinstance(s, pd.Series):
                raise TypeError
            if not is_numeric_dtype(s):
                raise ValueError

            self.__sUnnormalized = s
        except TypeError:
            print(f"Object passed is not a Series. Object is:{str(s)}" )
        except ValueError:
            print(f'Column is not numeric. It is {str(s.dtype)}')