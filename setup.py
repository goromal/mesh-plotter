#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

# get key package details from mesh_plotter/__version__.py
about = {}  # type: ignore
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'mesh_plotter', '__version__.py')) as f:
    exec(f.read(), about)

# load the README file and use it as the long_description for PyPI
with open('README.md', 'r') as f:
    readme = f.read()

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(
    name=about['__title__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=find_packages(exclude=('tests')),
    include_package_data=True,
    python_requires=">=3.6.*",
    install_requires=['numpy', 'matplotlib', 'geometry', 'pysignals'],
    license=about['__license__'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'mesh_plotter = mesh_plotter.cli:cli'
        ],
    },
)
