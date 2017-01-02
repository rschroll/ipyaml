#!/usr/bin/env python

from distutils.core import setup

setup(
    name='IPYaml',
    version='0.1',
    description='Alternate format for Jupyter notebooks',
    long_description='This package provides an extension for the Jupyter notebook server to allow it to read and write notebooks in a YAML file format.',
    author='Robert Schroll',
    author_email='rschroll@gmail.com',
    url='https://github.com/rschroll/ipyaml',
    packages=['ipyaml'],
    package_data={'ipyaml': ['nbext/*']},
    scripts=['ipyamlconvert'],
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
