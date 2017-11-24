import numpy as np
import scipy as sc
from scipy import interpolate


plist = [(3 , 1), (2.5, 4), (0, 1), (-2.5, 4),(-3, 0), (-2.5, -4), (0, -1), (2.5, -4), (3, -1),]

ctr=np.array(plist)

x=ctr[:,0]
y=ctr[:,1]

# uncomment both lines for a closed curve
#x=np.append(x,[x[0]])  
#y=np.append(y,[y[0]])

l=len(x)  

t=np.linspace(0,1,l-2,endpoint=True)
t=np.append([0,0,0],t)
t=np.append(t,[1,1,1])

tck=[t,[x,y],3]
u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
out = sc.interpolate.splev(u3,tck)

