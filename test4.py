from __future__ import print_function
import numpy as np
import numba 
from time import time # for comparing runing time
d, N = 512, 1000 # dimension, number of training points
X = np.random.randn(N, d) # N d-dimensional points
z = np.random.randn(d)

@numba.jit(nopython=False, parallel=True)
def dist_ps_fast(z, X):
    X2 = np.sum(X*X, 1) # square of l2 norm of each ROW of X
    z2 = np.sum(z*z) # square of l2 norm of z
    return X2 + z2 - 2*X.dot(z) # z2 can be ignored

X = dist_ps_fast(z,X)

