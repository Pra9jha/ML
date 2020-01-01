import pandas as pd
df1=pd.DataFrame({"city":["Delhi","mumbai","kolcatta","Hydrabad"],"temperature":[21,23,34,45]})
# print(df1)
print(df1["temperature"].apply(lambda x:x*2))

df1.sort_values(by=["temperature"],ascending=False,inplace=True)
print(df1)


