import numpy as np
import math

'these following function is for each radius in atom up to r'
def radwave2(n,l,r):
    Z = 1                                           #atomic constant
    a0 = 5.2917721067*(10**(-11))                   #bohr's constant
    K = np.full((1,r),(Z/(a0*n)))                   #radial constant for continuous r
    valueconv = np.full((1,r+1),(10**(-11)))        #to convert radius to meters
    R = range(1,r+1)                                #radial constant for continuous r
    rho = 2*K*R                                     #radial constant
    divideL = np.asarray(range(0,n-l))              #Laguerre polynomials
    narray = np.asarray(range(0,n-l))
    init_up_L = np.asarray(range(0,n-l))
    init_down_L = np.asarray(range(0,n-l))
    for i in narray:                                #Laguerre polynomials n,l
        init_up_L[i-1] = ((-1)**i)*((math.factorial(n+l))**2)*(rho**i)
        init_down_L[i-1] = math.factorial(i)*math.factorial(n-l-1-i)*math.factorial(2*l+1+i)
        divideL[i-1] = init_up_L[i-1]/init_down_L[i-1]
        L = np.sum(divideL)
    radwave2 = np.asarray(range(0,n-l))
    narray2 = np.asarray(range(1,r+1))
    for i in narray2:    
        radwave2[i-1] = ((2*Z/(n*a0))**(1.5))*((float(math.factorial(n-l-1))/float(2*n*(math.factorial(n+l)**3)))**0.5)*(np.exp(-Z*i/(n*a0)))*((2*Z*i/(n*a0))**l)*L
    return radwave2;
print "the second form of radial wave function at n l r is:",radwave2(4,0,100)
