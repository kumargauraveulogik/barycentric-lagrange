# cy_lagrange.pyx
import cython
import numpy as np
cimport numpy as np


cdef extern from "lagrange.hpp":
    cdef cppclass Lagrange:
        Lagrange(int,double*,int,double*)
        int ni       # Number of interpolation points
        int ne       # Number of evaluation points
        double* xi   # Interpolatio points
        double* xe   # Evaluation points
        double* w    # Barycentric weights
        double* ell  # ell(x) polynomial with roots at xi

        int bi_sum(double*,double*)            # Evaluate sums like eq. (4.2)
        int interp(int, double*, int, double*) # Evaluate the interpolant
        int get_ne()                           # Return number of eval points

cdef class Barycentric:
    cdef Lagrange *thisptr

    def __init__(self,np.ndarray[np.double_t,ndim=1] xi,
                      np.ndarray[np.double_t,ndim=1] xe):
        self.thisptr = new Lagrange(xi.size,<double *> xi.data,
                                    xe.size,<double *> xe.data)
    def __dealloc__(self):
        del self.thisptr 

    def bi_sum(self,np.ndarray[np.double_t,ndim=1] f,
                    np.ndarray[np.double_t,ndim=1] y):
        return self.thisptr.bi_sum(<double *> f.data,<double *> y.data)

    def get_ne(self):
        return self.thisptr.get_ne()

    def interp(self,np.ndarray[np.double_t,ndim=1] func):

        # Allocate a 1D NumPy array to write the evaluated polynomial
        cdef np.ndarray poly = np.zeros((self.get_ne(),), dtype = np.double)

        # Modify poly in place
        self.thisptr.interp(func.size,<double *> func.data,
                            poly.size,<double *> poly.data)
        return poly
