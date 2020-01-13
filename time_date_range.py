import pandas as pd
data_set=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/15_ts_date_range/aapl.csv",parse_dates=["Date"],index_col="Date")
#print(data_set["2017-06"].Close.mean())

#Range between two time
print(data_set["2017-06":"2018-06"])

