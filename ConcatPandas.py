import pandas as pd
data1={"city":["Mumbai","Bangaluru","Kolcatta"],"temperature":[38,40,34],"windspeed":[7,6,9]}
# print(data1)
data1=pd.DataFrame(data1)

data2={"city":["Nyork","Cikago","Calefornia"],"temperature":[28,20,24],"windspeed":[7,6,9]}
# print(data2)
data2=pd.DataFrame(data2)
data=pd.concat([data1,data2])
print(data)

print("***********************************************")
#Note here we are getting index starting from 0 again to fix it we can use ignore

data=pd.concat([data1,data2],ignore_index=True)
print(data)

#creating additional index as country name along with numerical index

df=pd.concat([data1,data2],keys=["India_weather","us_weather"])
print(df)


#To get data of us-weather only
df=df.loc["us_weather"]
print(df)


#using axis column

df=pd.concat([data1,data2],keys=["India_weather","us_weather"],axis=1)
print(df)





