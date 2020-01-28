import  pandas as pd,matplotlib.pyplot as plt,seaborn as sns
titanic_train_data=pd.read_csv("/Users/prashant/python/Pandas/Refactored_Py_DS_ML_Bootcamp-master/13-Logistic-Regression/titanic_train.csv")
# print(titanic_train_data.head())
#print(titanic_train_data.info())


#Check the null value
# print(titanic_train_data.isnull())
#sns.heatmap(titanic_train_data.isnull(),yticklabels=False,cbar=False,cmap='viridis')
# plt.show()
#from heat map it is clear there is null value in Age and Cabin column

#Checking who survived vs not survived
sns.set_style("whitegrid")
# sns.countplot(x="Survived",data=titanic_train_data)
# sns.countplot(x="Survived",data=titanic_train_data,hue="Sex")
# sns.countplot(x="Survived",data=titanic_train_data,hue="Pclass")
# sns.distplot(titanic_train_data["Age"].dropna(),kde=False,bins=30)
# sns.countplot(x="SibSp",data=titanic_train_data)
sns.barplot(x="SibSp",y="Survived",data=titanic_train_data)
plt.show( )


# Filling mishing data

# plt.figure(figsize=(10,7))
# sns.boxenplot(x='Pclass',y="Age",data=titanic_train_data)
# plt.show()

#From the box plot graph it is quite clear that most of the passenger in the
# first class is of the higher age then the passenger in the second or third
# class ,it's quite obvious as to bear 1st class ticket u need to make money and
# it takes time to make money
'''From boxplot Average age of passenger in first class is 37 , Average age 
 of passenger in second class is 29 and that of third class is 24'''


# Now we willl be filling the age column this method will fill the null
# value with the average age of the passenger of that class
def inpute_age(cols):
    Age=cols[0]
    Pclass =cols[1]
    if pd.isnull(Age):
        if Pclass==1:
            return 37
        elif Pclass==2:
            return 29
        else :
            return 24
    else:
        return Age

titanic_train_data["Age"]=titanic_train_data[["Age","Pclass"]].apply(inpute_age,axis=1)
# sns.heatmap(titanic_train_data.isnull(),yticklabels=False,cbar=False)
# plt.show()
#Now we have only cabin column as mishing data
titanic_train_data.drop("Cabin",axis=1,inplace=True)
print(titanic_train_data.info())
titanic_train_data.dropna(inplace=True)
#sns.heatmap(titanic_train_data.isnull(),yticklabels=False,cbar=False)
#plt.show()



'''Note cleaning of data is done so now we will use dummy to replace data of few columns'''
Sex=pd.get_dummies(titanic_train_data['Sex'],drop_first=True,)
Embarked=pd.get_dummies(titanic_train_data["Embarked"],drop_first=True)
titanic_train_data=pd.concat([titanic_train_data,Sex,Embarked],axis=1)#Here Sex and Embarked will be concatinated with the training data set
titanic_train_data.drop(["Sex","Embarked","Name","Ticket","PassengerId"],axis=1,inplace=True)

'''Using machine learning model on the data set'''

print(titanic_train_data.head()) #Final data set

x=titanic_train_data.drop("Survived",axis=1)
y=titanic_train_data["Survived"]


#Applying ML algorithm

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=101)

from sklearn.linear_model import LogisticRegression
logestic_module=LogisticRegression()
logestic_module.fit(X_train,Y_train)
prediction=logestic_module.predict(X_test)


from sklearn.metrics import classification_report

print(classification_report(Y_test,prediction))


from sklearn.metrics import  confusion_matrix

print(confusion_matrix(Y_test,prediction))