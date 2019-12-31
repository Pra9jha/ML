import pandas as pd
#importing data from csv file
data_frame=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/2_dataframe_basics/weather_data.csv")
# print(data_frame)



# Query to find rows where temperature is >=25
# print(data_frame[data_frame.temperature>25])


#Query to search rows with maximum value of the temperatre

print(data_frame[data_frame.temperature==data_frame.temperature.max()])
