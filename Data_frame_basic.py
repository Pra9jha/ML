import pandas as pd
#importing data from csv file
data_frame=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/2_dataframe_basics/weather_data.csv")
print(data_frame)

#print only specific column
# print(data_frame["temperature"])


# to describe temperatue
print(data_frame["temperature"].max())
print(data_frame["temperature"].mean())
print(data_frame["temperature"].min())
print(data_frame["temperature"].std())
print(data_frame["temperature"].describe())

#sorting on the basis of tempearture in descending order

# print(data_frame.sort_values(by=["temperature"],ascending=False).reset_index(drop=True))