import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


tips=sns.load_dataset("tips")
print(tips.head(5))


'''BarPlot'''
# #Sample barplot
# sns.barplot("sex","tip",data=tips)
# #barplot using estimator
# sns.barplot("sex","tip",data=tips,estimator=np.std)
# plt.show()


'''Countplot'''
# # g=tips.groupby("sex")
# # print(g.count())
# sns.countplot(x="sex",data=tips)
# plt.show()


'''boxplot shows distribution of quantitive data in a way that hopefullt facilitate comparasion between variables '''

# #sample boxplot
# # sns.boxenplot(x="day",y="total_bill",data=tips)
#
# #adding hue to boxplot
# sns.boxenplot(x="day",y="total_bill",data=tips,hue='smoker')
# plt.show()



'''violinplot is almost same as the boxplot '''
# #sampe violinplot
# sns.violinplot(x="day",y="total_bill",data=tips)

#violinplot with hue as smoker
# sns.violinplot(x="day",y="total_bill",data=tips,hue="smoker")

## now as we see we have two plot for each day so to ake it one with hue we can add split=True
# sns.violinplot(x="day",y="total_bill",data=tips,hue="smoker",split=True)
# plt.show()


'''strip plot '''
# #sample strip plot
# sns.stripplot(x="day",y="total_bill",data=tips,jitter=False,hue="sex",split=True)
# plt.show()
#

'''Most important is we can create any of the plot using catplot previously called "factorplot" just by passing as argument kind '''

sns.catplot(y="total_bill",x="day",data=tips,kind="bar",hue="sex")#note here we can change kind to stripplot,violinplot or any ither type of plot that we read till now
plt.savefig('day_vs_total-bill.png')#we can also save in pdf formate
plt.show()