import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from numpy import linalg as LA
from scipy.interpolate import BSpline
from scipy.misc import derivative
from radialwave import radialwave
from radialwave import V

# make r
n = 2
l = 1
r = np.arange(0,50,2.0)
waver = []

for i in r:
	fr = radialwave(n,l,i)
	waver.append(fr)

# we have points (r,waver) 

# first establish knot
t = np.arange(len(r))
#t *= 1.0/t.max()
print("first knots:",t)
count = len(r)
k = 4 #degree

kv = np.array([0]*k + range(count-k+1) + [count-k]*k)

print("knots:",kv)


splr = BSpline(kv,r,k) #spline r
splw = BSpline(kv,waver,k) #spline wr

tplot = np.arange(0,kv.max(),0.1)
#tplot *= 1.0/tplot.max()

rbspline = splr(tplot)
waverbspline = splw(tplot)
'''
plt.plot(r,waver,'bo')
plt.plot(r,waver,'k')
plt.plot(rbspline,waverbspline,'r')

#axes = plt.gca()
#axes.set_xlim([0,20])
#axes.set_ylim([0,0.2])
plt.show()
'''
## basis element

for i in range(len(kv)-k-2):
	b = BSpline.basis_element(kv[i+1:i+k+2])
	print(kv[i+1:i+k+2])
	x = np.linspace(kv[i+1], kv[i+k+2], 25)
	print(x)

'''	plt.plot(x, b(x))
plt.show()'''

#derivative
prod = (r[2]-r[1])/(x[2]-x[1])
ddb = derivative(b,(x*prod),n=2)

#hamiltonian
def integrand(x):
	return np.outer(b(x),ddb)

def integrand2(x):			
	return np.outer(b(x),b(x))/(x**2)

def integrand3(x):			
	return np.outer(b(x),b(x))*V(x)

Hb = integrate.simps(integrand(x),x)
Ha = integrate.simps(integrand2(x),x)
Hc = integrate.simps(integrand3(x),x)
H = prod*(-0.5*Ha+l*(l+1)*0.5*Hb+Hc)

np.set_printoptions(threshold=np.inf)
print("Hamiltonian:",H)

#overlap matrix S

def integrand4(x):
	return np.outer(b(x),b(x))

S = prod*integrate.simps(integrand4(x),x)
print("Overlap matrix S:",S)

# Hc = ESc, ES adalah eigenvalue dari H
Hx = np.matrix(H.reshape((5,5)))
v = LA.eigvals(Hx)
print('eigval:',v)
vector = LA.eig(Hx) #eigen vector

# ES = vI, E = vI*S'
E=np.amax(v)*np.identity(5)*LA.inv(S.reshape(5,5))
print('Energy:',E)

#plt.plot(r,waver)
#plt.show()
	
