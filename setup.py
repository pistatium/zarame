# coding: utf-8

import os
import sys
from setuptools import setup, find_packages

setup(
    name='zarame',
    version='0.0.1',
    url='https://github.com/pistatium/zarame',
    author='pistatium',
    description='Simple structural transducer using NamedTuple',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'test': [
            'pytest'
        ]
    }
)

