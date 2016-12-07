# -*- coding: utf-8 -*-

import os

from setuptools import find_packages
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='mobiledb',
    version='1.0.dev',
    description="",
    long_description="",

    author="Zhang Erning",
    url="https://github.com/erning/mobiledb-py",
    license='BSD',

    packages=[''],
    include_package_data=True,
    package_data={
        '': ['mobiledb.pickle']
    },

    zip_safe=True,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
