from production.DataProcessorForData_2021_11_15 import DataProcessorForData_2021_11_15
from production.DataProcessorNewAttr import DataProcessorNewAttr


dp = DataProcessorForData_2021_11_15()
processed_2021_11_15 = dp.process()

dp = DataProcessorNewAttr()
processed_New_Attr = dp.process()

