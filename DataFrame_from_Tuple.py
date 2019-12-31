import pandas as pd
weather_data=[("1/1/2017","32","6","Rain"),("1/2/2017","35","7","Sunny"),("1/3/2017","28","2","Snow"),]
df=pd.DataFrame(weather_data,columns=["date","temperatue","windspeed","event"])
print(df)
