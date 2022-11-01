## Cython: setup.py
from distutils.core import setup, Extension
from Cython.Build import cythonize

exts= (cythonize("planet_cy.pyx"))

setup(ext_modules = exts)

