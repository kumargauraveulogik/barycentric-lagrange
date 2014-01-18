# setup.py

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
import os


os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"


setup( name = 'lagrange',
       version = '0.1',
       author = 'Greg von Winckel',
       description = 'C++ class for Barycentric Lagrange inerpolation with Cython',
       ext_modules=[Extension("cy_lagrange",
                        sources=["cy_lagrange.pyx","lagrange.cpp"],
                        language="c++",
                        include_dirs=[numpy.get_include()])
       ],
       cmdclass = {'build_ext': build_ext},
)                                         
       

