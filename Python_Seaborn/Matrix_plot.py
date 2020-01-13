import matplotlib.pyplot as plt
import seaborn as sns
flights=sns.load_dataset("flights")
tips=sns.load_dataset("tips")
print(flights.head())
# print(tips.head())


'''Matrix plot : for matrix_plot we need to have same lables and indexes i'e column items should be same as row items'''
#here in flight and tips  data rows and column has no colleration so we can do it by calling correlation function

tips_corr=tips.corr()
print(tips_corr)

# #Now once we have correlation data we can plot matrix using heatmap for tips dataframe
# #sample heatmap
# sns.heatmap(data=tips_corr)
# #providing annotation and colormap to heatmap
# sns.heatmap(data=tips_corr,annot=True,cmap='coolwarm')
# plt.sho


# #we will use pivot for making data perfect for heatmap
#
# flights=flights.pivot_table(index="month",columns="year",values="passengers")
# print(flights)
#
# #Now once we have data we can plot matrix using heatmap for flight dataframe ,
# sns.heatmap(data=flights,annot=True,cmap="magma",linewidths=1)
# plt.show()
