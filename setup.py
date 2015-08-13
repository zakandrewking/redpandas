# -*- coding: utf-8 -*-

import sys
from os.path import join, dirname, realpath

try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

# get the version
directory = dirname(realpath(__file__))
sys.path.insert(0, join(directory, 'redpandas'))
version = __import__('version').__version__

class TestCommand(Command):
    description = "Run the redpandas tests."
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import pytest
        exit_code = pytest.main([])
        sys.exit(exit_code)

setup(name='redpandas',
      version=version,
      author='Zachary King',
      url='https://github.com/zakandrewking/redpandas',
      license='MIT',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: MIT License',
          'Topic :: Scientific/Engineering',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4'
      ],
      keywords='pandas, sql, data structures, data frames',
      packages=['redpandas'],
      install_requires=['pandas>=0.16.2'],
      extras_require={'all': ['pytest>=2.7.2']},
      cmdclass={'test': TestCommand})
