import pandas as pd
import numpy as np
data_frame=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/6_handling_missing_data_replace/weather_data.csv",parse_dates=["day"])
data_frame.set_index('day',inplace=True)
print(data_frame)



#Here if the dataframe is having some weired value which we want to replace with NAN and then perform some operation like fillna or dropna
data_frame=data_frame.replace({"temperature":-99999,"windspeed":-99999,"event":0},np.NAN)
print(data_frame)

#Now we can perform replace NAN with some value


data_frame.interpolate(method="linear",inplace=True)
print(data_frame.replace({"event":"0"},np.NAN,inplace=True))