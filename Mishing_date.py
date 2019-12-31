import pandas as pd
data_frame=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/5_handling_missing_data_fillna_dropna_interpolate/weather_data.csv",parse_dates=["day"])
dr=pd.date_range("01-01-2017","01-11-2017")
ind=pd.DatetimeIndex(dr)
data_frame=data_frame.reindex(ind)
print(data_frame)