import matplotlib.pyplot as plt
import numpy as np
from radialwave import radialwave

# make r
n = 2
l = 1
r = np.arange(0,20,0.01)
waver = []

for i in r:
	fr = radialwave(n,l,i)
	waver.append(fr)


plt.plot(r,waver)
plt.show()
	
