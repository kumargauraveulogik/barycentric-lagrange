# setup.py

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import os


os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"


setup( name = 'lagrange',
       version = '0.1',
       author = 'Greg von Winckel',
       description = 'C++ class for Barycentric Lagrange inerpolation with Cython',
       ext_modules=[Extension("cy_lagrange",
                        sources=["cy_lagrange.pyx","lagrange.cpp"],
                        language="c++")
       ],
       cmdclass = {'build_ext': build_ext},
)                                         
       
#       ext_modules = cythonize("cy_lagrange.pyx",
#                sources = ["lagrange.cpp"],
#                extra_compile_args = ['-fopenmp'],
#                extra_link_args= [ '-lgomp'],
#                language="c++",))        
