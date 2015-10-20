#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Tue 20 Oct 2015 15:31:08 CEST

from setuptools import setup, find_packages

# Define package version
version = open("version.txt").read().rstrip()

setup(
    name='bob.db.cohface',
    version=version,
    description="Bob Database interface for the COHFACE database",
    keywords=['bob', 'database', 'cohface'],
    url='http://gitlab.idiap.ch/biometric/bob.db.cohface',
    license='BSD',
    author='Andre Anjos',
    author_email='andre.anjos@idiap.ch',

    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    namespace_packages = [
        'bob',
        'bob.db',
    ],

    entry_points = {
        'bob.db': [
            'cohface = bob.db.cohface.driver:Interface',
            ],
      },

    install_requires=[
      'setuptools',
      'bob.db.base',
      'bob.io.video',
      'bob.ip.facedetect',
      'mne',
      ],

    classifiers=[
      'Framework :: Bob',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Topic :: Software Development :: Libraries :: Python Modules',
      ],

    )
