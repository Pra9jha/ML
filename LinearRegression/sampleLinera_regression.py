import pandas as pd, numpy as np , matplotlib.pyplot as plot,seaborn as sns
coordibnate_points={"x":[1,2,3,4,5],"y":[3,4,2,4,5]}
coordibnate_points=pd.DataFrame(coordibnate_points)
# print(coordibnate_points)
# sns.lmplot(x="x",y="y",data=coordibnate_points)
#Ploting coordinate
plt=sns.scatterplot(x="x",y="y",data=coordibnate_points)

#Now to find regression line we for this equation y=mx+c ,here m and c is unknown so we we have to find value od ma and c

X_mean=coordibnate_points["x"].mean()
Y_mean=coordibnate_points["y"].mean()

'''m=summation(x-X_mean)(y-Y_mean)/x-X_mean)^2'''

coordibnate_points["a"]=[x-X_mean for x in coordibnate_points["x"]]
coordibnate_points["b"]=[y-Y_mean for y in coordibnate_points["y"]]
coordibnate_points["c"]=[i**2 for i in coordibnate_points["a"]]
coordibnate_points["d"]=[i*j for i,j in zip(coordibnate_points["a"],coordibnate_points["b"])]
print(coordibnate_points)
# print(sumxminusX_mean)
# print(sumyminusY_mean)

m=coordibnate_points["d"].sum()/coordibnate_points["c"].sum()
print("slop is "+str(m))


#now we have y,x,m out of  y=mx+c y_mean=3.6 ,x_mean=3 ,m=04


c=Y_mean-(X_mean*m)

print("value of c is "+ str(c))


#Now we have the ma nd c so we can draw linear regression line so we will find Yp i.e y predicted as per the equation

Yp=lambda x:(m*x)+c

map_value=list(map(Yp,coordibnate_points["x"]))
coordibnate_points["Yp"]=list(map_value)

print(coordibnate_points)
coordibnate_points.drop(columns=["a","c","d"],inplace=True)

coordibnate_points["c"]=[i**2 for i in coordibnate_points["b"]]
coordibnate_points["d"]=[i-Y_mean for i in coordibnate_points["Yp"]]
coordibnate_points["e"]=[i**2 for i in coordibnate_points["d"]]
print(coordibnate_points)

# sns.stripplot(x="x",y="Yp",data=coordibnate_points)

#Now we will find R^2 to see the error

R_square=coordibnate_points["c"].sum()/coordibnate_points["e"].sum()
print(R_square)

#As the value is 3.2 so this is not good module for data analysis
plt=sns.lmplot(x="x",y="y",data=coordibnate_points)

plot.show()
