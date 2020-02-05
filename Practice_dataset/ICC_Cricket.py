import pandas as pd,numpy as np,seaborn as sns,matplotlib.pyplot as plt,math

cricket_dataset=pd.read_csv("/Users/prashant/python/Pandas/Practice_dataset/ICC_Test_Batting_Figures.csv",encoding='latin1').drop(["Span","0","Player Profile","HS"],axis=1)
# print(cricket_dataset.info())
# print(cricket_dataset.head()

element_list=[]
for columns in cricket_dataset.columns.drop("Player"):
    # print(columns + " : "+str(cricket_dataset[columns].dtype))
    if cricket_dataset[columns].dtype=="object":
       for element in cricket_dataset[columns]:
           if element!="-":
               element_list.append(float(element))
           else:
               element_list.append(np.nan)
       # print("columns length "+str(len(cricket_dataset[columns])))
       # print("change vlaue length "+str(len(element_list)))
       cricket_dataset[columns]=element_list
       element_list.clear()
# cricket_dataset.to_csv("TestBatsman.csv")


# print(cricket_dataset.isnull())
# sns.heatmap(cricket_dataset.isnull(),yticklabels=False,cbar=False)
# plt.show()

def fill_avg(cols):
    run=cols[0]
    inn=cols[1]
    avg=cols[2]
    if pd.isnull(avg) and pd.notnull(run) and pd.notnull(inn):
        avg=run/inn
    return avg




cricket_dataset["Avg"]=cricket_dataset[["Runs","Inn","Avg"]].apply(fill_avg,axis=1)

cricket_dataset.dropna(inplace=True)
# print(cricket_dataset.isnull())


from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
scaler=StandardScaler()
scaler.fit(cricket_dataset.drop('Player',axis=1))
scaler_feature=scaler.transform(cricket_dataset.drop('Player',axis=1))

cricket_standard_dataset=pd.DataFrame(scaler_feature,columns=cricket_dataset.columns.drop("Player"))
# cricket_standard_dataset["Player"]=cricket_dataset["Player"]
# print(cricket_standard_dataset.head())


def point_calculater(cols):
    match=cols[0]
    inn=cols[1]
    no=cols[2]
    runs=cols[3]
    avg=cols[4]
    hund=cols[5]
    fifty=cols[6]
    return 0.25*match+0.5*inn+runs+0.12*no+3*avg+0.5*hund+0.75*fifty


cricket_dataset["Point"]=cricket_standard_dataset.apply(point_calculater,axis=1)
cricket_dataset=cricket_dataset.sort_values(by="Point",ascending=False,)
cricket_dataset.reset_index(drop=True,inplace=True)

# cricket_dataset.set_index(pd.Index(range(0,len(cricket_dataset))),inplace=True)
catagory=1
catagory_list=[]
for i in range(len(cricket_dataset["Point"])):
    # print(str(i)+"------->"+str(cricket_dataset.iloc[i][["Player","Point"]]))
    # print("catagory is "+str(catagory))
    catagory_list.append(catagory)
    if i%596==0 and i>0 or i==100 or i==400:
        catagory=catagory+1


cricket_dataset["catagory"]=catagory_list
# print(cricket_dataset.head())
cricket_dataset.to_csv("TestBatsman_point.csv")
# print(cricket_dataset.describe().round(2))


#Up to now we have catagorised the dataset now we will use ml for future prediction

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error


scaler=StandardScaler()
scaler.fit(cricket_dataset.drop(["catagory","Player","Point"],axis=1))
scaler_feature=scaler.transform(cricket_dataset.drop(["catagory","Player","Point"],axis=1))
cricket_scaler_data=pd.DataFrame(scaler_feature,columns=["Mat","Inn","NO","Runs","Avg","100","50"])
x=cricket_scaler_data
y=cricket_dataset["catagory"]
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=180)


# error=[]
# for k in range(1,50):
#     knn=KNeighborsClassifier(n_neighbors=k)
#     knn.fit(X_train,Y_train)
#     prediction = knn.predict(X_test)
#     error.append(mean_squared_error(Y_test,prediction))
#
# sns.lineplot(range(1,50),error)
# plt.savefig("ICC_test_module_error1.pdf")

print(X_test)

knn=KNeighborsClassifier(n_neighbors=12)
knn.fit(X_train,Y_train)
prediction=knn.predict(X_test)

print(classification_report(Y_test,prediction))
print("**************************************")
print(confusion_matrix(Y_test,prediction))





