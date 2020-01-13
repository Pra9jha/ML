import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
print(tips.head())

# # sns.set_style('darkgrid')
# # sns.set_style('ticks')
# sns.set_style('whitegrid')
# sns.countplot(x="sex",data=tips)
# sns.despine(left=True,bottom=True) #This will remove line from botttom and left

# plt.figure(figsize=(12,8))
# sns.set_style('whitegrid')
# sns.countplot(x="sex",data=tips)
# sns.despine(left=True,bottom=True) #This will remove line from botttom and left
# plt.show()


sns.set_context('poster',font_scale=3)#notebook
sns.countplot(x="sex",data=tips)
sns.despine(left=True,bottom=True) #This will remove line from botttom and left
plt.show()


plt.show()