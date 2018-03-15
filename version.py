from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
# _version_major = 0
# _version_minor = 1
# _version_micro = ''  # use '' for first of series, number for 1 and above
# _version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
# _ver = [_version_major, _version_minor]
# if _version_micro:
    # _ver.append(_version_micro)
# if _version_extra:
    # _ver.append(_version_extra)

# __version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 2 - Pre-Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Natural Language :: English",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "waste_not_the_water: a data science tool for wastewater treatment"
# Long description will go up on the pypi page
long_description = """

waste_not_the_water
========
waste_not_the_water is a data science tool for urban wastewater treatment plants.

It contains two different components, a predictive machine learning model and 
data visualization. All the data is taken from the open source database from the 
Urban Waste Water Treatment Directive from the European Commission.

For more information about our project, checkout out the repository 
README_.

.. _README: https://github.com/parkec3/waste_not_the_water/blob/master/README.md

License
=======
``waste_not_the_water`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.
"""

NAME = "waste_not_the_water"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "https://github.com/parkec3/waste_not_the_water"
DOWNLOAD_URL = "https://github.com/parkec3/waste_not_the_water/tags"
LICENSE = "MIT"
AUTHOR = "Caitlin Parke"
AUTHOR_EMAIL = "parkec3@uw.edu"
PLATFORMS = "OS Independent"
# MAJOR = _version_major
# MINOR = _version_minor
# MICRO = _version_micro
# VERSION = __version__
PACKAGE_DATA = {'waste_not_the_water': [pjoin('data', '*')]}
REQUIRES = ["numpy"]
