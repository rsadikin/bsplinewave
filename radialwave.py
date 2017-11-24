import numpy as np
import math

#the following program is used to find radial wave function analytically.
'''
calculating radial wave function steps:
1. defining constants for partial radial solution
2. laguerre polynomials
3. radial wave function
'''

from sympy import var
from sympy.physics.hydrogen import R_nl


def radialwave(n,l,r):
    Z = 1                                                   #atomic constant
    var("r Z")
    radialwave = eval('R_nl(n,l,r,Z)')
    return radialwave;

'''
    a0 = 0.47560075833827875#5.2917721067*(10**(-11))       #bohr's constant in cgs
    K = (float(Z)/float(a0))*n                              #partial Kappa constant
    R = r*10**(-11)#5.2917721067*(10**(-11))                #radial constant for single r in atomic unit
    rho = 2*K*R                                             #partial Rho constant
    divideL = np.asarray(range(0,n-l))                      #Laguerre polynomials
    narray = np.asarray(range(0,n-l))
    for i in narray:                                        #Laguerre polynomials n,l loop
        divideL[i-1] = (((-1)**i)*((math.factorial(n+l))**2)*(rho**i))/(math.factorial(i)*math.factorial(n-l-1-i)*math.factorial(2*l+1+i))
        L = np.sum(divideL)
    radialwave = ((2*Z/(n*a0))**(1.5))*((float(math.factorial(n-l-1))/float(2*n*(math.factorial(n+l)**3)))**0.5)*(np.exp(-Z*R/(n*a0)))*((2*Z*R/(n*a0))**l)*L                                               #radial wave function at r with Laguerre polynomials
'''
print "the radial wave function at n l r is:",radialwave(4,0,6)


