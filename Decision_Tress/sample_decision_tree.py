import pandas as pd ,numpy as np, matplotlib.pyplot as plt ,seaborn as sns
df=pd.read_csv("/Users/prashant/python/Pandas/Refactored_Py_DS_ML_Bootcamp-master/15-Decision-Trees-and-Random-Forests/kyphosis.csv")
# print(df.head())
# print("**********************************************")
# print(df.describe())
# print("**********************************************")
# print(df.info())

# sns.pairplot(df,hue="Kyphosis")
# plt.show()

# sns.heatmap(df.isnull())
# plt.show()



from sklearn.model_selection import  train_test_split

X=df.drop("Kyphosis",axis=1)
Y=df["Kyphosis"]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)



algo='''Decision Tress classification'''
print(algo)

from  sklearn.tree import DecisionTreeClassifier
dtree=DecisionTreeClassifier()
dtree.fit(X_train,Y_train)

prediction=dtree.predict(X_test)
from  sklearn.metrics import classification_report,confusion_matrix

print(confusion_matrix(Y_test,prediction))
print("*************************************************************************")
print(classification_report(Y_test,prediction),end="\n\n")



algo='''Random Forest '''
print(algo)

from sklearn.ensemble import RandomForestClassifier #Decision tree in inside ensemble instred of tree because it's bunch of decision tree

rfc=RandomForestClassifier(n_estimators=200)
rfc.fit(X_train,Y_train)
rfc_predict=rfc.predict(X_test)

print(confusion_matrix(Y_test,rfc_predict))
print("*************************************************************************")
print(classification_report(Y_test,rfc_predict))


