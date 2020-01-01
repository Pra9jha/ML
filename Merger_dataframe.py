import pandas as pd
df1=pd.DataFrame({"city":["Delhi","mumbai","kolcatta","Hydrabad"],"temperature":[21,23,34,45]})
df2=pd.DataFrame({"city":["Delhi","mumbai","kolcatta"],"humidity":[6,8,14,]})

print(df1)
print(df2)
#note how can have left , rgight ,outer ,inner
#indicator=True will define where the dataframe come from


df=pd.merge(df1,df2,on="city",how="outer",indicator=True)
print(df)

