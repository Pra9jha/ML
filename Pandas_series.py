import pandas as pd
import numpy as np
lables=['a','b','c']
my_data= [10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}
series=pd.Series(data=my_data,index=lables)
print(series)