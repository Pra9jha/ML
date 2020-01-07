import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,11)
y=x**2
print(x)
print(y)


#there are two ways of creating plot using Matplotlib 1> Functional and 2> Object Oriented
#Functional
plt.plot(x,y,'r-') #Here r- is the color of the plot
plt.xlabel("X label")
plt.ylabel("Y label")
plt.title("y=x**2")

# plt.show()



#WE can have multiplot on the same canvash
plt.subplot(1,2,1)
plt.plot(x,y,'-r')

plt.subplot(1,2,2)
plt.plot(x,y,'-b')
plt.show()