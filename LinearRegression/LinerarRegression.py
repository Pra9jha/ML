import pandas as pd ,numpy as np,matplotlib.pyplot as plt,seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
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
# sns.heatmap(USA_Housing_data.corr(),annot=True)
# plt.show()

x=USA_Housing_data[["Avg. Area Income","Avg. Area House Age","Avg. Area Number of Rooms","Avg. Area Number of Bedrooms","Area Population",]]
y=USA_Housing_data["Price"]
#print(x)
#print(y)

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.4,random_state=101)
# print(X_train)
# print(X_test)
# print(Y_train)
# print(Y_test)
lm=LinearRegression()
lm.fit(X_train,Y_train)
intercept=lm.intercept_
# print(intercept)
coef=lm.coef_
# print(coef)
cdf=pd.DataFrame(lm.coef_,x.columns,columns=['coeff'])
# print(cdf)

#Prediction and error


# print(Y_test)
Y_prediction=lm.predict(X_test)
# print(Y_prediction)

#Now to see how close we are of the actual test data
# plt.scatter(Y_test,prediction)
# plt.show()

#Note if the graph has normal behaviour then the linear regression model is the correct choice
# sns.distplot(Y_test-Y_prediction)
# plt.show()

#Calculating error metrix
from sklearn import metrics
mae=metrics.mean_absolute_error(Y_test,Y_prediction)
print(mae)
mse=metrics.mean_squared_error(Y_test,Y_prediction)
print(mse)
rmse=np.sqrt(mse)
print(rmse)
