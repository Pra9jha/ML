import pandas as pd
#Note here key of all the dictionary is same
weather_data=[{'day':'1/1/2019' ,'temperature':30,'windspeed':6,'event':'rain'},{'day':'1/2/2019' ,'temperature':35,'windspeed':7,'event':'sunny'},
              {'day':'1/3/2019' ,'temperature':38,'windspeed':9,'event':'rain'}]
df=pd.DataFrame(weather_data)
print(df)

#If the key differs as in firast dictionary i have made day as date

weather_data=[{'date':'1/1/2019' ,'temperature':30,'windspeed':6,'event':'rain'},{'day':'1/2/2019' ,'temperature':35,'windspeed':7,'event':'sunny'},
              {'day':'1/3/2019' ,'temperature':38,'windspeed':9,'event':'rain'}]
df=pd.DataFrame(weather_data)

print(df)