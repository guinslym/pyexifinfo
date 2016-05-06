#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Imports
from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path
import sys
from check_requirements import check_if_exiftool_is_already_installed
from check_requirements import print_a_header


result = check_if_exiftool_is_already_installed()

if not result:
    sys.exit()
else:
    print_a_header("Great Exiftool is installed on your system!")

#Begin the installation
here = path.abspath(path.dirname(__file__))

setup(
    name='PyExifinfo',

    version='0.1.7',

    description="Simple Metadata extraction using Exiftool",

    url='https://github.com/guinslym/pyexifinfo',

    author='Guinslym',
    author_email='guinslym@gmail.com',

    license='GNU GPLv2',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
    ],

    keywords='exiftool reader stats metadata image linux',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),


)
