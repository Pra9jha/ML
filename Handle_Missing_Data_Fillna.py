import pandas as pd
#importing data from csv file
# data_frame=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/2_dataframe_basics/weather_data.csv")
# print(data_frame)

#Note day is of string type here
#print(type(data_frame["day"][0]))


#for better visulisation we will convert day to date type for that we uses parse_date with list of columns
data_frame=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/5_handling_missing_data_fillna_dropna_interpolate/weather_data.csv",parse_dates=["day"])
data_frame.set_index('day',inplace=True)
print(data_frame)


#Now we need to replace all the NaN values with 0 using method filllna
data_frame1=data_frame.fillna(0) # Here all the NaN will be replaced with 0
print(data_frame1)

# To change value of Na with some value which differ from column to column
data_frame1=data_frame.fillna({"temperature":0,"windspeed":0,"event":"data not available"})
print(data_frame1)


#Replace value of the NaN , we can specify method type in filna method we can use ffill and bfill for forwardfill and backward fill
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html

data_frame1=data_frame.fillna(method='bfill')
print(data_frame1)
data_frame1=data_frame.fillna(method='ffill')
print(data_frame1)

#Note Here in fillna method axis by default it is rows

data_frame1=data_frame.fillna(method='bfill',axis="columns")
print(data_frame1)

#Note we can also specify limit in fillna method





