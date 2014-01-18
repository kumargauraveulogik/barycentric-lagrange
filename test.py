import numpy as np
import numpy.polynomial.chebyshev as C
import time
from scipy.interpolate import BarycentricInterpolator as bi
from cy_lagrange import Barycentric

if __name__ == '__main__':

    ni = 500
    ne = 20000

    # Interpolation points
    xi = C.chebpts1(ni)

    # Evalutation points
    xe = np.linspace(-1,1,ne)

    # The data to interpolate
    fi = np.sin(10*xi)*np.exp(xi)
 
    t = [time.time()]
    
    # Interpolate using Cython/C++
    bary = Barycentric(xi,xe)

    t.append(time.time())    
 
    fe = bary.interp(fi)

    t.append(time.time())    

    # Interpolate using SciPy's BarycentricInterpolator
    L = bi(xi)
    L.set_yi(fi)

    t.append(time.time())    

    ge = L(xe)

    t.append(time.time())    

    cy_init_time = t[1]-t[0]
    cy_eval_time = t[2]-t[1]
    sp_init_time = t[3]-t[2]
    sp_eval_time = t[4]-t[3]

    print('Cython init time = %.6f' % cy_init_time)
    print('Cython eval time = %.6f' % cy_eval_time)
    print('SciPy init time = %.6f' % sp_init_time)
    print('SciPy eval time = %.6f' % sp_eval_time)


