#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
import pandas as pd
data_frame=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/5_handling_missing_data_fillna_dropna_interpolate/weather_data.csv",parse_dates=["day"])
data_frame.set_index('day',inplace=True)

#interpolation without any method specified will give linear interpolation , it's never so accurate
df1=data_frame.interpolate()
print(data_frame)

#Here we will use method="time"

df2=data_frame.interpolate(method="time",str="linear")
print(df2)