import pandas as pd

class Normalizer:
    def __init__(self, listForSeries=[]):
        self.set_sUnnormalized(listForSeries)
        self.decimalPlaces = 15
        self.sUnnormalized = pd.Series().round(decimals=self.decimalPlaces)


    def normalize(self):
        s_min_max_scaled = self.__sUnnormalized
        s_min_max_scaled = (s_min_max_scaled - s_min_max_scaled.min()) / (s_min_max_scaled.max() - s_min_max_scaled.min())
        return s_min_max_scaled.round(self.decimalPlaces)


    def set_sUnnormalized(self, s):
        try:
            if isinstance(s, pd.Series):
                raise TypeError

            self.__sUnnormalized = pd.Series(s)
        except TypeError:
            print(f"Object passed is not a Series. Object is:{str(s)}" )