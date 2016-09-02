from distutils.core import setup
from Cython.Build import cythonize

ext_modules = cythonize(['*.pyx'])
ext_modules[0].sources.append('nanoclock_impl.c')

setup(
  name = 'ftimer',
  ext_modules = ext_modules,
)
