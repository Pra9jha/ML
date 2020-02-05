import pandas as pd, seaborn as sns,matplotlib.pyplot as plt,numpy as np
project_data=pd.read_csv("/Users/prashant/python/Pandas/Refactored_Py_DS_ML_Bootcamp-master/14-K-Nearest-Neighbors/KNN_Project_Data")
print(project_data.info())
print(project_data.head())


# sns.heatmap(project_data.isnull(),yticklabels=False,linecolor='black')
# plt.show()


# sns.pairplot(project_data,hue='TARGET CLASS',palette='coolwarm')
# plt.show()
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(project_data.drop('TARGET CLASS',axis=1),project_data['TARGET CLASS'])
scaler_feature=scaler.transform(project_data.drop('TARGET CLASS',axis=1))
# print(scaler_feature)
project_standerized_data=pd.DataFrame(scaler_feature,columns=project_data.columns.drop('TARGET CLASS'))
# print(project_standerized_data)


from sklearn.model_selection import  train_test_split
x=project_standerized_data
y=project_data['TARGET CLASS']
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=101)


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix

error=[]
for k in range(1,50):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train,Y_train)
    prediction=knn.predict(X_test)
    from sklearn.metrics import  mean_squared_error
    error.append(mean_squared_error(Y_test,prediction))


# sns.lineplot(range(1,50),error,markers="*",markerfacecolor='red', markersize=10,linestyle='dashed')
# plt.title('Error Rate vs. K Value')
# plt.xlabel('K')
# plt.ylabel('Error Rate')
# plt.savefig("sample_project.pdf")



knn=KNeighborsClassifier(n_neighbors=int(input("Enter the value of the k for minimum possible error")))
knn.fit(X_train,Y_train)
prediction=knn.predict(X_test)
print(len(prediction))
df=pd.DataFrame({'Y_test':Y_test,'prediction':prediction})
print(df)




print(classification_report(Y_test,prediction))
print(confusion_matrix(Y_test,prediction))
