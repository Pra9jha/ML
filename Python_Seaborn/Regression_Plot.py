import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
print(tips.head())
#Sample plot for Regression
sns.lmplot(x="total_bill",y="tip",data=tips)

#lmplot with additional argumrnt
sns.lmplot(x="total_bill",y="tip",data=tips,hue="sex",markers=["o","v"])

#here we will replace hue with col so it will create two plot on the basis of sex
sns.lmplot(x="total_bill",y="tip",data=tips,col="sex")


#Hrre we can specify rows also
sns.lmplot(x="total_bill",y="tip",data=tips,col="sex",row="time")

plt.show()