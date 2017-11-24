import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import BSpline
from radialwave import radialwave

# make r
n = 2
l = 1
r = np.arange(0,20,2.0)
waver = []

for i in r:
	fr = radialwave(n,l,i)
	waver.append(fr)

# we have points (r,waver) 

# first establish knot
t = np.arange(len(r))
#t *= 1.0/t.max()
print(t)
count = len(r)
k = 4 #degree


kv = np.array([0]*k + range(count-k+1) + [count-k]*k)

print(kv)


splr = BSpline(kv,r,k) #spline r
splw = BSpline(kv,waver,k) #spline wr


tplot = np.arange(0,kv.max(),0.1)
#tplot *= 1.0/tplot.max()

rbspline = splr(tplot)
waverbspline = splw(tplot)

#plt.plot(r,waver,'bo')
#plt.plot(r,waver,'k')
#plt.plot(rbspline,waverbspline,'r')

#axes = plt.gca()
#axes.set_xlim([0,20])
#axes.set_ylim([0,0.2])
#plt.show()



## basis element
k = 4
for i in range(len(kv)-k-2):
	b = BSpline.basis_element(kv[i+1:i+k+2])
	print(b)
	print(kv[i+1:i+k+2])
	x = np.linspace(kv[i+1], kv[i+k+2], 51)
	print(x)
	plt.plot(x, b(x))
plt.show()


#plt.plot(r,waver)
#plt.show()
	
