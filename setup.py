import os
import re
import subprocess

import setuptools

directory = os.path.dirname(os.path.abspath(__file__))

# version
init_path = os.path.join(directory, 'prefixcommons', '__init__.py')
with open(init_path) as read_file:
    text = read_file.read()
version = '0.1.4'


setuptools.setup(
    name='prefixcommons',
    version=version,
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
    ]
)
