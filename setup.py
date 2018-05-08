import os
import re
import sys
import subprocess

import setuptools

# get version
exec(open('prefixcommons/version.py').read())

if sys.version_info.major < 3:
    sys.exit("Error: Python 3 is required")

directory = os.path.dirname(os.path.abspath(__file__))

# version
#init_path = os.path.join(directory, 'prefixcommons', '__init__.py')
#with open(init_path) as read_file:
#    text = read_file.read()


setuptools.setup(
    name='prefixcommons',
    version = __version__,
    author='Chris Mungall',
    author_email='cmungall@gmail.com',
    url='https://github.com/prefixcommons/prefixcommons',
    description='Library for working prefixcommons.org CURIEs',
    long_description=open("README.rst").read(),
    license='BSD3',
    packages=['prefixcommons'],

    keywords='ontology graph obo owl sparql networkx network',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],

    # Dependencies
    install_requires=[
        'pyyaml',
        'requests',
        'cachier'
    ],

    scripts=['bin/curie-csv.py'],
    
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        #'dev': ['plotly'],
        'test': ['pytest'],
    },
 )
