import pandas as pd
weather_data=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/7_group_by/weather_by_cities.csv")
#print(weather_data)

df=pd.DataFrame(weather_data)
# print(df)
g=df.groupby('city')
# print(g)
for i,j in g:
    print(i)
    print("***********")
    print(j)

print(g.get_group('mumbai'))

#Here we will find maximum temoperature in each of the cities

print(g.max())

print(g.mean)

print(g.describe)

#Here this procress is also called split ,apply and combine

