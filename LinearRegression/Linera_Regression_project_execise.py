import pandas as pd,seaborn as sns,matplotlib.pyplot as plt, numpy as np
ecdata=pd.read_csv("/Users/prashant/python/Pandas/Refactored_Py_DS_ML_Bootcamp-master/11-Linear-Regression/Ecommerce_Customers.csv")

# priting dataset and info
# print(ecdata.head())
# print(ecdata.info())
#print(ecdata.describe())


#Checking null value
# print(len(ecdata))
ecdata.dropna(inplace=True)
# print(len(ecdata))

#Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns. Does the correlation make sense?
# sns.jointplot(ecdata["Time on Website"],ecdata["Yearly Amount Spent"])
# plt.show()


#Use seaborn to create a jointplot to compare the Time on Mobile app and Yearly Amount Spent columns. Does the correlation make sense?
# sns.jointplot(ecdata["Time on App"],ecdata["Yearly Amount Spent"])
# plt.show()

#Now we will plot both the graph with kind= hex
# sns.jointplot(ecdata["Time on Website"],ecdata["Yearly Amount Spent"],kind="hex")
# sns.jointplot(ecdata["Time on App"],ecdata["Yearly Amount Spent"],kind="hex")
# plt.show()


#Let's explore these types of relationships across the entire data set. Use pairplot to recreate the plot below.(Don't worry about the the colors)
#sns.pairplot(ecdata)
#plt.show()

#*Create a linear model plot (using seaborn's lmplot) of Yearly Amount Spent vs. Length of Membership. *

# sns.lmplot("Length of Membership","Yearly Amount Spent",data=ecdata)
# plt.show()

from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.model_selection import train_test_split
x=ecdata[["Avg. Session Length","Time on App","Time on Website","Length of Membership"]]
y=ecdata["Yearly Amount Spent"]

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=101)
# print(X_train)
# print("**********************************************************************")
# print(X_test)
# print("**********************************************************************")
# print(Y_train)
# print("**********************************************************************")
# print(Y_test)

lr=LinearRegression().fit(X_train,Y_train)
lr_intercept=lr.intercept_
lr_coef=lr.coef_
# print(lr_intercept)
# print(lr_coef)
ec_coeff=pd.DataFrame(lr_coef,x.columns,columns=["Yearly Amount Spent"])
print(ec_coeff)

#Prediction
Y_prediction=lr.predict(X_test)
# print(y_prediction)
# print(len(X_test))
# print(len(Y_test))
# print(len(y_prediction))
# df=pd.DataFrame(Y_prediction)
# print(df)

# plt=sns.scatterplot(x=Y_test,y=Y_prediction)
# plt.show()

from sklearn import  metrics
mse=metrics.mean_squared_error(Y_test,Y_prediction)
print("vale of mse is :     "+ str(mse))

sns.distplot(Y_test-Y_prediction)
plt.show()

'''After looking into the coefficient report we can draw conclusion that with increase 
in 1unit of Avg. Session Length Yearly amount increases to 25.981550  similarly comparing
all the depenent variable we can say that mobile app works better here but the most
influential factor is the Length of membership
'''