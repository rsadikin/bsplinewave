import numpy as np
import scipy as sc
from scipy import misc
import math


Unl = np.sum(cB)

#loop
B[] = ((x-t[i])/(t[i+k-1]-t[i])) B[] + ((t[i+k]-x)/(t[i+k]-t[i+1])) B[]

f = B(x)
#derivative B
dB = sc.misc.derivative(f,1.0,dx=1e-6)
#or:
dB2 = ((k-1)/(t[i+k-1]-t[i])) B[] + ((k-1)/(t[i+k]-t[i+1])) B[]
#print dB
