#!/usr/bin/env python
""" 
  Package setup/installation for lambdata_edchin
  Workflow:
            Make & test code changes locally
            Update version=(new version number) in setup.py & utils_edchin/__init__.py
            Create distributions files : Saves a compressed version of the code in the "dist" dir
                      python setup.py sdist bdist_wheel    
            Upload the package to the test PyPI server, where it can be downloaded by others via pip commands                              
                      twine upload --repository-url https://test.pypi.org/legacy/ dist/* 
"""

import setuptools

REQUIRED = [
    'numpy',
    'pandas',
    'sklearn'
    ]

# get the Long Description from Readme.md
with open('README.md','r') as fh:
  LONG_DESCRIPTION = fh.read()


# Docs : https://setuptools.readthedocs.io/en/latest/setuptools.html#command-reference
# Go to "New and Changed setup() Keywords "
setuptools.setup(
    name='utils-edchin',
    version='1.0.9',
    author='Ed Chin',
    description="Personal Data Science Utilities in Python",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/ed-chin-git/Utils_edchin',
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    install_requires=REQUIRED,
    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",]
     )
