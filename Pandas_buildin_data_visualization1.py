import numpy as np ,pandas as pd , matplotlib.pyplot as plt ,seaborn as sns
data_set=pd.read_csv("/Users/prashant/python/Pandas/tutorial/py/pandas/15_ts_date_range/aapl.csv",parse_dates=["Date"],index_col="Date")
print(data_set)

#Here we are ploting hist graph
# data_set["Open"].hist(bins=40)
# plt.show()

#we can specify plot as an argument in the datafram plt method

# data_set["Volume"].plot(kind="hist",bins=30)
# plt.show()


#we can directly cll plot type method of plot call

# data_set["Low"].plot.hist()
# plt.show()


# data_set[["Open","High"]].plot.area(alpha=0.4)
# plt.show()

#bar takes indev value as a catagorical
# data_set[["Open","High","Low"]].plot.bar()
# plt.show()

#
# data_set.plot.scatter(x="Close",y="Open",c='C') #here c is color
# plt.show()

data_set[["Open","Close"]].plot.box()
plt.show()
