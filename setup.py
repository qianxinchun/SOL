#! /usr/bin/env python
#################################################################################
#     File Name           :     lsol/setup.py.in
#     Created By          :     yuewu
#     Description         :      
#################################################################################

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

import sys
import os

sys.path.append("python/lsol")

def get_source_files(root_dir):
    src_files = []
    for pathname in os.listdir(root_dir):
        path = os.path.join(root_dir, pathname)
        if os.path.isfile(path):
            src_files.append(path)
        elif os.path.isdir(path):
            src_files = src_files + get_source_files(path)
    return src_files

ext_modules = [
    Extension(
        "pylsol",
        sources=["python/lsol/pylsol.pyx"] + get_source_files('src/lsol'),
        language='c++',
        include_dirs=[np.get_include(), "include", "external"],
        extra_compile_args = ['-DHAS_NUMPY_DEV','-DUSE_STD_THREAD', '-std=c++11']
        )
]

setup(name='lsol',
        version='',
        description='Library for Scalable Online Learning',
        author='Yue Wu, Chenghao Liu, Steven C.H. Hoi',
        author_email='yuewu@outlook.com',
        maintainer='Yue Wu, Chenghao Liu',
        maintainer_email='yuewu@outlook.com',
        url='http://libsol.stevenhoi.org',
        license='Apache 2.0',
        packages=['lsol'],
        package_dir={'':'python'},
        package_data={},
        ext_modules=cythonize(ext_modules))