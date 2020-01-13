import pandas as pd ,numpy as np,matplotlib.pyplot as plt,seaborn as sns
USA_Housing_data=pd.read_csv("/Users/prashant/python/Pandas/Refactored_Py_DS_ML_Bootcamp-master/11-Linear-Regression/USA_Housing.csv")
# print(USA_Housing_data.info())
# print(USA_Housing_data.describe())
# print(USA_Housing_data.columns)
# sns.pairplot(USA_Housing_data)
# plt.show()
# plt.savefig("USA_Housing_data.png")
#HERE WE WILL CHECK DISTRIBUTION OF THE COLUMN WE ANT TO PREDICT WE WILL GO FOR PRICE COLUMN

# sns.distplot(USA_Housing_data.Price)
# plt.show()

#we can also check the corelation between columns using heatmap

# print(USA_Housing_data.corr().head())
sns.heatmap(USA_Housing_data.corr(),annot=True)
plt.show()