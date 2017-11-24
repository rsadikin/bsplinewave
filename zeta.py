import numpy as np
import math

#define breakpoints
#linear sequence
def zetalinear(rmax, rmin, n):
    zetalinear = np.asarray(range(1,n))
    narray = np.asarray(range(1,n))
    for i in narray:
        zetalinear[i-1] = rmin+((rmax-rmin)/(n-1))*(i-1)
    return zetalinear;
print "linear results are:", zetalinear(100, 0, 21)

#exponent sequence
def zetaexponent(rmax, rmin, n, G):
    zetaexponent = np.asarray(range(1,n))
    narray = np.asarray(range(1,n))
    for i in narray:
        zetaexponent[i-1] = rmin+(rmax-rmin)*(math.exp(G)*float(i-1)/float(n-1)-1)/(math.exp(G)-1) #hasilnya belum membentuk kurva eksponensial
    return zetaexponent;
print "exponent results are:", zetaexponent(100, 0, 21, 6)

#sinelike sequence
def zetasin(rmax, rmin, n, alpha):
    zetasin = np.asarray(range(1,n))
    narray = np.asarray(range(1,n))
    for i in narray:
         zetasin[i-1] = rmin+rmax*np.sin((math.pi/2)*((float(i-1)/float(n-1)**alpha))) #hasilnya belum membentuk kurva sinusial
    return zetasin;
print "sinelike results are:", zetasin(100, 0, 21, 2)

#linear-parabolic sequence
def zetalinpara(rmax, rmin, n, io):
    zetalinpara = np.asarray(range(1,n))
    narray = np.asarray(range(1,n))
    ro = (rmax*(io-1)+rmin*(n-io))/(2*n-io-1)
    alpha = (ro-rmin)/((io-1)**2)
    beta = (rmax-ro)/(n-io)
    if i<io and i>=1 in narray:
       zetalinpara = rmin+alpha*((i-1)**2)
    elif i<n and i>=io:
       zetalinpara = ro+beta*(i-io) #hasilnya tidak dalam bentuk array
    return zetalinpara;
print "linear-parabolic results are:", zetalinpara(100, 0, 21, 2)

#linear-parabolic2 sequence
def zetalinpara2(rmax, rmin, n, io):
    zetalinpara = np.asarray(range(1,n))
    narray = np.asarray(range(1,n))
    zetazero = (rmax*(io-1)+rmin*(n-io))/(2*n-io-1)
    ro = np.full((1,n-1),zetazero)
    alphazero = (ro-rmin)/((io-1)**2)
    alpha = np.full((1,n-1),alphazero)
    betazero = (rmax-ro)/(n-io)
    beta = np.full((1,n-1),betazero)
    for i in narray:
        if i<io and i>=1:
           zetalinpara2 = rmin+alpha*((i-1)**2)
        elif i<n and i>=io:
           zetalinpara2 = ro+beta*(i-io) #hasilnya dalam bentuk array tapi entah kenapa sama semua nilainya
    return zetalinpara2;
print "linear-parabolic2 results are:", zetalinpara2(100, 0, 21, 2)
