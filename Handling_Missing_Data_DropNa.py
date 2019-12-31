import pandas as pd
data_frame=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/5_handling_missing_data_fillna_dropna_interpolate/weather_data.csv",parse_dates=["day"])

#Drop na will drop all the rows having any of the na values
df=data_frame.dropna()
print(df)

print("******************************************************")
#Note we can set the threshold that if there is more than 1 na value then only drop the rows

df1=data_frame.dropna(thresh=1)
print(df1)

