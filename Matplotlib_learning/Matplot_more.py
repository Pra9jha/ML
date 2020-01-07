import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5,11)
y=x**2
fig=plt.figure()
axes=fig.add_axes([0,0,1,1])
axes.plot(x,y,color="purple")
plt.show()