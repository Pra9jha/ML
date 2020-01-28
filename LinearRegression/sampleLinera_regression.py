import pandas as pd, numpy as np , matplotlib.pyplot as plot,seaborn as sns
coordinate_point={"x":[1,2,3,4,5],"y":[3,4,2,4,5]}
coordinate_point=pd.DataFrame(coordinate_point)
# print(coordinate_point)
# sns.lmplot(x="x",y="y",data=coordinate_point)
#Ploting coordinate
plt=sns.scatterplot(x="x",y="y",data=coordinate_point)

#Now to find regression line we for this equation y=mx+c ,here m and c is unknown so we we have to find value od ma and c

X_mean=coordinate_point["x"].mean()
Y_mean=coordinate_point["y"].mean()

'''m=summation(x-X_mean)(y-Y_mean)/x-X_mean)^2'''

coordinate_point["a"]=[x-X_mean for x in coordinate_point["x"]]
coordinate_point["b"]=[y-Y_mean for y in coordinate_point["y"]]
coordinate_point["c"]=[i**2 for i in coordinate_point["a"]]
coordinate_point["d"]=[i*j for i,j in zip(coordinate_point["a"],coordinate_point["b"])]
print(coordinate_point)
# print(sumxminusX_mean)
# print(sumyminusY_mean)

m=coordinate_point["d"].sum()/coordinate_point["c"].sum()
print("slop is "+str(m))


#now we have y,x,m out of  y=mx+c y_mean=3.6 ,x_mean=3 ,m=04


c=Y_mean-(X_mean*m)

print("value of c is "+ str(c))


#Now we have the ma nd c so we can draw linear regression line so we will find Yp i.e y predicted as per the equation

Yp=lambda x:(m*x)+c

map_value=list(map(Yp,coordinate_point["x"]))
coordinate_point["Yp"]=list(map_value)

print(coordinate_point)
coordinate_point.drop(columns=["a","c","d"],inplace=True)

coordinate_point["c"]=[i**2 for i in coordinate_point["b"]]
coordinate_point["d"]=[i-Y_mean for i in coordinate_point["Yp"]]
coordinate_point["e"]=[i**2 for i in coordinate_point["d"]]
print(coordinate_point)

# sns.stripplot(x="x",y="Yp",data=coordinate_point)

#Now we will find R^2 to see the error

R_square=coordinate_point["c"].sum()/coordinate_point["e"].sum()
print(R_square)

#As the value is 3.2 so this is not good module for data analysis
plt=sns.lmplot(x="x",y="y",data=coordinate_point)

plot.show()
