# -*- coding: utf-8 -*-
"""
    setup
    ~~~~
    Flask-Pymodm is a simple plugin to integrate Pymodm.
    :copyright: (c) 2019 by Petru Buzulan, Daniele Dapuzzo.
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup

from flask_pymodm import __version__


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name='Flask-Pymodm',
    version=__version__,
    url='https://github.com/pbuzulan/flask-pymodm',
    project_urls={
        "Documentation": "",
        "Code": "https://github.com/pbuzulan/flask-pymodm",
        "Issue tracker": "https://github.com/pbuzulan/flask-pymodm/issues",
    },
    license='MIT',
    author=['Petru Buzulan', 'Daniele Dapuzzo'],
    author_email=['buzulan.petru@gmail.com', 'dapuzzo.dapuzzo92@gmail.com'],
    description="Flask-Pymodm is a simple plugin for Pymodm",
    long_description=open('README.rst').read(),
    packages=['flask_pymodm'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=parse_requirements('requirements.txt'),
    tests_require=[

    ],
    test_suite='tests',
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
