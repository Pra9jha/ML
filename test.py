import pandas as pd ,matplotlib.pyplot as plt,seaborn as sns
dic={"x":[1,2,3,4,5],"y":[4,3,7,4,90]}
df=pd.DataFrame(dic)
# print(df)
# # sns.lmplot(x="x",y="y",data=df)
# # plt.show()
# sns.distplot(df["y"],bins=100)
# plt.show()

def add(value):
    if value[1]>value[0]:
        return value[1]
    else :
        return  value[0]



df["x"]=df[["x","y"]].apply(add,axis=1)

print(df.set_index(keys="x",drop=True))