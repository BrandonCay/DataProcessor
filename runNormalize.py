from production.DataProcessorNewAttr import DataProcessorNewAttr
from data.proccessedPythonData import processed_New_Attr
import pandas as pd

def main():
    processed_New_Attr.to_csv("data/newAttributeNormalized.csv",  index = False)

if(__name__ == '__main__'):
    main()
    
    