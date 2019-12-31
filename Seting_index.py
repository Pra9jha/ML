import pandas as pd
#importing data from csv file
data_frame=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/2_dataframe_basics/weather_data.csv")
# print(data_frame)

# Making one of the column as the index
# data_frame.set_index('day',inplace=True)
# print(data_frame)

# Making an index which start from 1
index=[i for i in range(1,len(data_frame)+1)]
data_frame["index"]=index
data_frame.set_index('index',inplace=True)
print(data_frame)
