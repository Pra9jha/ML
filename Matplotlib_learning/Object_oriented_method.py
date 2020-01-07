import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,11)
y=x**2
# print(x)
# print(y)


#Object Oriented

# fig=plt.figure()
# axes1=fig.add_axes([0.1,0.1,0.8,0.8])
# axes1.plot(x,y,"-r")
# axes1.set_title("Larger Plot")
# axes2=fig.add_axes([0.2,0.5,0.3,0.3])
# axes2.plot(y,x,"-b")
# axes2.set_title("Smaller Plot")
# plt.show()


#Subplot using object oriented method

fig=plt.figure()
fig,axes=plt.subplots(nrows=1,ncols=2)
axes.legend(loc=0)
axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Second Plot')
plt.show()