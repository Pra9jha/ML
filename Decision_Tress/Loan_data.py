import pandas as pd, matplotlib.pyplot as plt,seaborn as sns
loan_data=pd.read_csv("/Users/prashant/python/Pandas/Refactored_Py_DS_ML_Bootcamp-master/15-Decision-Trees-and-Random-Forests/loan_data.csv")
# print(loan_data.head())
# print("*******************************************")
# print(loan_data.describe())
# print("*******************************************")

# purpose=pd.get_dummies(loan_data["purpose"])
purpose_list=loan_data["purpose"].unique()

purpose_and_not_paid={}
for element in purpose_list:
    purpose_and_not_paid[element]=0
# print(purpose_and_not_paid)



for element in range(len(loan_data)):
    # print(loan_data["purpose"][element],end="   --->  ")
    # print(purpose_and_not_paid[loan_data["purpose"][element]])
    if loan_data["not.fully.paid"][element]==1:
        # print(loan_data["purpose"][element],end=" ")
        # print(loan_data["not.fully.paid"][element])
        purpose_and_not_paid[loan_data["purpose"][element]]=purpose_and_not_paid[loan_data["purpose"][element]]+1

# print(purpose_and_not_paid)

purpose_number=dict(loan_data.groupby("purpose")["not.fully.paid"].count())
# print(purpose_number)

for purpose in purpose_number.keys():
    purpose_and_not_paid[purpose]=(purpose_and_not_paid[purpose]/purpose_number[purpose]).round(2)

# print(purpose_and_not_paid)

'''Ploting purpose and average of not.fully.paid '''
# sns.barplot(list(purpose_and_not_paid.keys()),list(purpose_and_not_paid.values()))
# plt.show()

# sns.countplot(x='purpose',hue='not.fully.paid',data=loan_data,palette='Set1')
# plt.show()

# sns.barplot(x="purpose",y="not.fully.paid",data=loan_data)
# plt.show()

# print(list(purpose_list).index("major_purchase"))
for element in range(len(loan_data["purpose"])):
    # print(loan_data["purpose"][element])
    # print(list(purpose_list).index(loan_data["purpose"][element]))
    loan_data["purpose"][element]=list(purpose_list).index(loan_data["purpose"][element])

# print(loan_data)


'''splitting data into train and test'''

from sklearn.model_selection import train_test_split

X=loan_data.drop("not.fully.paid",axis=1)
Y=loan_data["not.fully.paid"]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=101)


algorithm='''Decision Tree '''
print(algorithm)


from sklearn.tree import DecisionTreeClassifier

dtree=DecisionTreeClassifier()
dtree.fit(X_train,Y_train)

prediction=dtree.predict(X_test)
print(prediction)

from sklearn.metrics import classification_report,confusion_matrix


print(confusion_matrix(Y_test,prediction))
print("**************************************")
print(classification_report(Y_test,prediction))



algorithm='''Random Forest '''
print(algorithm)

from sklearn.ensemble import RandomForestClassifier

rforest=RandomForestClassifier(n_estimators=600)
rforest.fit(X_train,Y_train)
r_prediction=rforest.predict(X_test)

print(confusion_matrix(Y_test,r_prediction))
print("**************************************")
print(classification_report(Y_test,r_prediction))

