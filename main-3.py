
import numpy as np

o=0
yhat=np.random.rand(1,100)
y=np.random.randint(2,size=100)

for i in range(0,100):
    o=o+y[i]*np.log2(yhat[0][i])+(1-y[i])*np.log2(1-yhat[0][i])
    
o=-1/100*o
print('o')