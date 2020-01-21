import pandas as pd ,matplotlib.pyplot as plt,seaborn as sns
dic={"x":[1,2,3,4,5],"y":[4,3,7,4,9],"z":[2,3,5,8,9]}
df=pd.DataFrame(dic)
print(df)
sns.lmplot(x="x",y="y",data=df)
plt.show()