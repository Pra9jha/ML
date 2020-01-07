import seaborn as sns
import matplotlib.pyplot as plt
#This will load a data set name tips
tips=sns.load_dataset("tips")
# print(tips.head(10))

'''Here we will plot total_bill column as x axis and how many times this amount has been payed using displot '''

# #Sample displot
# sns.distplot(tips["total_bill"],bins=30)
#
# #sample displot with kde value is True
# sns.distplot(tips["total_bill"],bins=30,kde=True)
# plt.show()



'''Here we will see jointplot which is basically ploting one column with respect to other'''


# #smaple jointplot
# sns.jointplot("total_bill","tip",data=tips)
#
# #Hexagonal jointplot
# sns.jointplot("total_bill","tip",data=tips,kind="hex")
#
# #Regration jointplot
# sns.jointplot("total_bill","tip",data=tips,kind="reg")
#
# #kde jointplot to show density
# sns.jointplot("total_bill","tip",data=tips,kind="kde")
#
#
# plt.show()
#


''' Now we will see the pair plot which will dplot graph for all the numerical value in the dataset '''

# #sample pairplot
# sns.pairplot(tips)
#
# #Pair plot with hue value ,hue value will differntiate the specified columns element as here we will pass sex as hue value
# sns.pairplot(tips,hue="sex")
#
# plt.show()


'''Here we will see rugplot '''

#sample rugplot
#
# sns.rugplot(tips["total_bill"])
# plt.show()

'''If we just want to print kde plot'''
sns.kdeplot(tips["total_bill"])
plt.show()