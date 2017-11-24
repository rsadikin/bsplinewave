import numpy as np
from numpy import linalg as LA

#rewrite array
a = np.array([[1,1],[3,2]])



mat = np.matrix(a)

v = LA.eigvals(a)
np.savetxt('eigenvalue.txt', v, fmt='%.4f')

w, c = LA.eig(mat)
w; c

with open('eigenvector.txt','wb') as f:
    for line in c:
        np.savetxt(f, line, fmt='%.2f')
