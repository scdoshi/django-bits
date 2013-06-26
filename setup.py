#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = __import__('bits').__version__

setup(
    name="django-bits",
    version=VERSION,
    author='Siddharth Doshi',
    author_email='scdoshi@gmail.com',
    description=("Basic utilities and helpers for django projects"),
    long_description=open('README.md').read(),
    packages=find_packages(),
    url="http://github.com/scdoshi/django-bits/",
    license='Simplified BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
