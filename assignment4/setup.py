
from distutils.core import setup
from Cython.Build import cythonize


setup(
   name = "Mandelbrot",
   ext_modules = cythonize("*.pyx"),

)
