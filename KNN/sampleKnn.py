import pandas as pd,matplotlib.pyplot as plt,seaborn as sns,numpy as np
classified_data=pd.read_csv("/Users/prashant/python/Pandas/Refactored_Py_DS_ML_Bootcamp-master/14-K-Nearest-Neighbors/Classified Data").drop('Unnamed: 0',axis=1)
print(classified_data.info())
# print(classified_data.head())

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(classified_data.drop('TARGET CLASS',axis=1))
scaled_feature=scaler.transform(classified_data.drop('TARGET CLASS',axis=1))
classified_data_feat=pd.DataFrame(scaled_feature,columns=classified_data.columns[:-1])
#print(classified_data_feat.head())
# sizeWTT=len(list(classified_data_feat["EQW"]))
# sum=0
# for value in list(classified_data_feat["EQW"]):
#     sum=sum+value
# print(round(sum/sizeWTT,2))

from sklearn.model_selection import train_test_split
x=classified_data_feat
y=classified_data["TARGET CLASS"]
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=109)

from sklearn.neighbors import KNeighborsClassifier

#Ploting Graph for error


from sklearn.metrics import mean_squared_error
# error=[]
# for k_value in range(1,50):
#     knn=KNeighborsClassifier(n_neighbors=k_value)
#     knn.fit(X_train,Y_train)
#     prediction=knn.predict(X_test)
#     error.append(mean_squared_error(Y_test,prediction))
#
# sns.lineplot(x=range(1,50),y=error)
# plt.savefig("error_plot.pdf")


import time
time.sleep(5)

knn=KNeighborsClassifier(n_neighbors=int(input("Enter value of 'K' for the best prediction  :> ")))
knn.fit(X_train,Y_train)


# print(X_test.iloc[-1:])
# data_to_Predict=X_test.iloc[-1:]
# prediction=knn.predict(data_to_Predict)
# print(prediction)




prediction=knn.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print("************  confusion metrics for yhe Y_test and prediction ***********")
print(confusion_matrix(Y_test,prediction))
print("************classification_report ************")

print(classification_report(Y_test,prediction))









