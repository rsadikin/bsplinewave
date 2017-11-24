import numpy as np
import scipy.interpolate as si


def bsplineradialwave(zeta, degree=3):
    """ Calculate n samples on a bspline

        cv :      Array ov control vertices
        n  :      Number of samples to return
        degree:   Curve degree
        periodic: True - Curve is closed
                  False - Curve is open
    """

    # If periodic, extend the point array by count+degree+1
    zeta = np.asarray(zeta)
    count = len(zeta)

    if periodic:
        factor, fraction = divmod(count+degree+1, count)
        zeta = np.concatenate((zeta,) * factor + (zeta[:fraction],))
        count = len(zeta)
        degree = np.clip(degree,1,degree)

    # If opened, prevent degree from exceeding count-1
    else:
        degree = np.clip(degree,1,count-1)


    # Calculate knot vector
    kv = None
    if periodic:
        kv = np.arange(0-degree,count+degree+degree-1,dtype='int')
    else:
        kv = np.array([0]*degree + range(count-degree+1) + [count-degree]*degree,dtype='int')

    # Calculate query range
    u = np.linspace(periodic,(count-degree),n)


    # Calculate result
    arange = np.arange(len(u))
    points = np.zeros((len(u),cv.shape[1]))
    for i in xrange(cv.shape[1]):
        points[arange,i] = si.splev(u, (kv,cv[:,i],degree))

    return points

import matplotlib.pyplot as plt
colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')

cv = np.array([[ 50.,  25.],
   [ 59.,  12.],
   [ 50.,  10.],
   [ 57.,   2.],
   [ 40.,   4.],
   [ 40.,   14.]])

plt.plot(cv[:,0],cv[:,1], 'o-', label='Control Points')

for d in range(1,21):
    p = bspline(cv,n=100,degree=d,periodic=True)
    x,y = p.T
    plt.plot(x,y,'k-',label='Degree %s'%d,color=colors[d%len(colors)])

plt.minorticks_on()
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(35, 70)
plt.ylim(0, 30)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
