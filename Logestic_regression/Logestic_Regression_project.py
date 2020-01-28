import pandas as pd,matplotlib.pyplot as plt,seaborn as sns

'''Datas anaalysis and preparing data to fit ML module'''
advertising_data=pd.read_csv("/Users/prashant/python/Pandas/Refactored_Py_DS_ML_Bootcamp-master/13-Logistic-Regression/advertising.csv")
print(advertising_data.info())
# print(advertising_data.head())
# print(advertising_data.describe())

# #Histogram for Age
# sns.set_style('whitegrid')
# sns.countplot(advertising_data.Age)
# plt.show()

# #Create a jointplot showing Area Income versus Age
# sns.jointplot(x="Age",y="Area Income",data=advertising_data)
# plt.show()

# # Create a jointplot showing the kde distributions of Daily Time spent on site vs. Age
# sns.jointplot(x='Age',y='Daily Time Spent on Site',data=advertising_data,color='red',kind='kde')
# plt.show()


# #Create a jointplot of 'Daily Time Spent on Site' vs. 'Daily Internet Usage
# sns.jointplot(y="Daily Time Spent on Site",x="Daily Internet Usage",data=advertising_data,kind="kde",color="blue")
# plt.show()

# #Finally, create a pairplot with the hue defined by the 'Clicked on Ad' column feature
# sns.pairplot(data=advertising_data,hue="Clicked on Ad")
# plt.show()

# #Ananlysing "Clicked on Ad" data with other parameter
# sns.boxenplot(y="Age",x="Clicked on Ad",data=advertising_data)
# plt.show()
#
# sns.boxenplot(y="Daily Internet Usage",x="Clicked on Ad",data=advertising_data)
# plt.show()
#
#
# sns.boxenplot(y="Area Income",x="Clicked on Ad",data=advertising_data)
# plt.show()


#checking null value if its there there
# print(advertising_data.isnull())
# sns.heatmap(advertising_data.isnull(),yticklabels=False,cbar=False)
# plt.show()
#As shown in data there is no null, value in the dataset


'''Applying ML module on the data set'''
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrix

advertising_data.drop(["Daily Time Spent on Site","Ad Topic Line","City","Country","Timestamp"],axis=1,inplace=True)
x=advertising_data.drop(["Clicked on Ad"],axis=1)
y=advertising_data["Clicked on Ad"]


X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=104)
logisticmodel=LogisticRegression()
logisticmodel.fit(X_train,Y_train)
prediction=logisticmodel.predict(X_test)
print(prediction)
print(metrix.classification_report(Y_test,prediction))
print(metrix.confusion_matrix(Y_test,prediction))




# X_train,X_test,Y_train,Y_test=train_test_split()


