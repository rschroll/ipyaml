#!/usr/bin/env python

from distutils.core import setup

setup(
    name='NbClean',
    version='0.1',
    description='Clean ipynb files on save',
    long_description='Clean ipynb files on save',
    author='Robert Schroll',
    author_email='rschroll@gmail.com',
    url='https://github.com/rschroll/ipyaml',
    packages=['nbclean'],
    package_data={'nbclean': ['nbext/*']},
    scripts=['cleanipynb'],
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ]
)
