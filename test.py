import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.chebyshev as C
import time
from scipy.interpolate import BarycentricInterpolator as bi
from lagrange import Barycentric

if __name__ == '__main__':

    ni = 250
    ne = 100000

    # Interpolation points
    xi = C.chebpts1(ni)

    # Evalutation points
    xe = np.linspace(-1,1,ne)

    # The data to interpolate
    fi = np.sin(10*xi)*np.exp(xi)

    # Interpolate using Cython/C++/OpenMP
    start = time.time()
    bary = Barycentric(xi,xe)
    stop = time.time()
    cy_init_time = stop-start
    start = stop
    fe = bary.interp(fi)
    stop = time.time()
    cy_eval_time = stop-start

    # Interpolate using SciPy's BarycentricInterpolator
    start = time.time()
    L = bi(xi)
    L.set_yi(fi)
    stop = time.time()
    sp_init_time = stop-start
    start = stop
    ge = L(xe)
    stop = time.time()
    sp_eval_time = stop-start

    print('Cython init time = %.6f' % cy_init_time)
    print('Cython eval time = %.6f' % cy_eval_time)
    print('SciPy init time = %.6f' % sp_init_time)
    print('SciPy eval time = %.6f' % sp_eval_time)

 
    fig = plt.figure(1,(16,7))
    ax1 = fig.add_subplot(121)
    ax1.plot(xi,fi,'o',xe,fe)
    ax1.set_title('C++, Cython, and OpenMP')

    ax2 = fig.add_subplot(122)
    ax2.plot(xi,fi,'o',xe,ge)
    ax2.set_title('scipy.interpolate.BarycentricInterpolate')
    plt.show()
