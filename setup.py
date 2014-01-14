# setup.py

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


setup( name = 'lagrange',
       version = '0.1',
       author = 'Greg von Winckel',
       description = 'C++ class for Barycentric Lagrange inerpolation with Cython',
       ext_modules = [Extension("lagrange",["cy_lagrange.pyx","lagrange.cpp"],
                      language="c++")], 
                      extra_compile_args=['-fopenmp'],
                      extra_link_args=['-fopenmp'],
                      cmdclass={"build_ext":build_ext})        
