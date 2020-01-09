# -*- coding: utf-8 -*-
"""
    setup
    ~~~~
    Flask-Pymodm is a simple plugin to integrate Pymodm.
    :copyright: (c) 2019 by Petru Buzulan, Daniele Dapuzzo.
    :license: MIT, see LICENSE for more details.
"""

from setuptools import setup
import re, io

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('flask_pymodm/__version__.py'
            '', encoding='utf_8_sig').read()
).group(1)

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name='Flask-Pymodm',
    version=__version__,
    url='https://github.com/pbuzulan/flask-pymodm',
    project_urls={
        "Documentation": "https://pbuzulan.github.io/flask-pymodm/",
        "Code": "https://github.com/pbuzulan/flask-pymodm",
        "Issue tracker": "https://github.com/pbuzulan/flask-pymodm/issues",
    },
    license='MIT',
    author='Petru Buzulan, Daniele Dapuzzo',
    author_email='buzulan.petru@gmail.com, daniele.dapuzzo92@gmail.com',
    description="Flask-Pymodm is a simple plugin for Pymodm",
    long_description=long_description,
    long_description_content_type='text/markdown',
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
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
