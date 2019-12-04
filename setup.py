# -*- coding: utf-8 -*-
"""
    setup
    ~~~~
    Flask-Pymodm is a simple plugin to integrate Pymodm.
    :copyright: (c) 2019 by Petru Buzulan, Daniele Dapuzzo.
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup
from os.path import join, dirname

with open(join(dirname(__file__), 'flask_pymodm/__version__.py'), 'r') as f:
    exec(f.read())

with open(join(dirname(__file__), 'requirements.txt'), 'r') as f:
    install_requires = f.read().split("\n")

setup(
    name='Flask-Pymodm',
    version=__version__,
    url='https://github.com/corydolphin/flask-cors',
    license='MIT',
    author=['Petru Buzulan', 'Daniele Dapuzzo'],
    author_email=['buzulan.petru@gmail.com', 'dapuzzo.dapuzzo92@gmail.com'],
    description="Flask-Pymodm is a simple plugin for Pymodm",
    long_description=open('README.rst').read(),
    packages=['flask_pymodm'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=install_requires,
    tests_require=[
        'nose'
    ],
    test_suite='nose.collector',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
