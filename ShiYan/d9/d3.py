
import numpy as np
import pandas
x =  np.array(range(1,11)).reshape(2,5)
a = pandas.DataFrame( x ,index=[0,1] , columns= ['a','b','c','d','e'])
print(a)
print("================")
print(a.T)