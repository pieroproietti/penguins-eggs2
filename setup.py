#!/usr/bin/env python3
# coding: utf-8
from setuptools import find_packages, setup

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='eggs',
    description='port di eggs in python3',
    version='0.6',
    long_description=long_description,
    author='Piero Proietti',
    author_email='piero.proietti@gmail.com',
    url='https://github.com/pieroproietti/penguins-eggs2',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        ('License :: OSI Approved :: GNU Library or Lesser '
         'General Public License (LGPL)'),
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)