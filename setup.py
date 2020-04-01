#!/usr/bin/env python
# Always prefer setuptools over distutils
from setuptools import setup, find_packages

__doc__ = """
To install as system package:

  python setup.py install
  
To install as local package:

  RU=/opt/control
  python setup.py egg_info --egg-base=tmp install --root=$RU/files --no-compile \
    --install-lib=lib/python/site-packages --install-scripts=ds

-------------------------------------------------------------------------------
"""

print(__doc__)

version = open('VERSION').read().strip()
scripts = ['./scripts/PyStateComposer']
license = 'GPL-3.0'

package_data = {
    '': ['VERSION'],
}

setup(name='tangods-PyStateComposer',
      version=version,
      license=license,
      description='Tango device for calculating new states and attributes '
                  'from existing Tango Device Servers',
      packages=find_packages(),
      scripts=scripts,
      include_package_data=True,
      package_data=package_data
     )
