#Pivot allows to reshape or transform data

import pandas as pd
df=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/10_pivot/weather.csv")
print(df)
#Here we want date as a row and city to be in the column
print("************************************************************************")
df1=df.pivot(index="date",columns="city")
print(df1)


#Here if I want only humidity as a value present in the output dataframe
print("************************************************************************")
df2=df.pivot(index="date",columns="city",values="humidity")
print(df2)


#Now we will have index as city and date as column
print("************************************************************************")
df3=df.pivot(index="city",columns="date")
print(df3)


#Now above it is averaging the value of temperature and humidity value so we can use aggfunc to specify the value
print("************************************************************************")
df3=df.pivot(index="city",columns="date",aggfunc="sum")
print(df3)

