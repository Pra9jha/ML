import matplotlib.pyplot as plt
import seaborn as sns
iris=sns.load_dataset("iris")
tips=sns.load_dataset("tips")
print(iris.head())
print(iris["species"].unique())

# sns.pairplot(iris)

# g=sns.PairGrid(iris)
# g.map(plt.scatter)


# g=sns.PairGrid(iris)
# g.map_diag(sns.distplot)
# g.map_upper(plt.scatter)
# g.map_lower(sns.kdeplot)

g=sns.FacetGrid(data=tips,col="time",row="smoker")
g.map(sns.distplot,'total_bill')


plt.show()



