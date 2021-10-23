import pandas as pd

class Normalizer:
    def __init__(self, df):
        self.__dfUnnormalized = pd.DataFrame()
        
        print(df())

        self.set_dfUnnormalized(df)

    def normalize(self, strColumnName=""):
        column = strColumnName
        print("HNT" + str(self.__dfUnnormalized))
        df_min_max_scaled = self.__dfUnnormalized
        df_min_max_scaled[column] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (df_min_max_scaled[column].max() - df_min_max_scaled[column].min())
        return df_min_max_scaled

    def set_dfUnnormalized(self, df):
        try:
            if isinstance(df, pd.DataFrame):
                raise TypeError

            self.__dfUnnormalized = df
        except TypeError as T:
            print(f"Object passed is not a DataFrame. Object is:{str(df)}" )