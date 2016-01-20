#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Wed 30 Sep 2015 12:14:50 CEST

import os
from .models import *
from .driver import Interface, DATABASE_LOCATION

from pkg_resources import resource_filename

class Database(object):


  def __init__(self, dbdir=DATABASE_LOCATION):
    self.info = Interface()

    self.metadata = []
    for path, dirs, files in os.walk(dbdir):
      if 'data.hdf5' in files: #object directory
        relpath = os.path.relpath(path, dbdir)
        self.metadata.append(os.path.join(relpath, 'data'))


  def objects(self, protocol=None):
    """Returns a list of unique :py:class:`.File` objects for the specific
    query by the user.

    Returns: A list of :py:class:`.File` objects.
    """

    if protocol in ('train_all',):
      d = resource_filename(__name__, os.path.join('data', 'train_all.txt'))
      with open(d, 'rt') as f: sessions = f.read().split()
      return [File(k) for k in self.metadata if k in sessions]
    
    if protocol in ('train_clean')
      d = resource_filename(__name__, os.path.join('data', 'train_clean.txt'))
      with open(d, 'rt') as f: sessions = f.read().split()
      return [File(k) for k in self.metadata if k in sessions]

    if protocol in ('dev_clean')
      d = resource_filename(__name__, os.path.join('data', 'dev_clean.txt'))
      with open(d, 'rt') as f: sessions = f.read().split()
      return [File(k) for k in self.metadata if k in sessions]
    
    if protocol in ('dev_all',):
      d = resource_filename(__name__, os.path.join('data', 'dev_all.txt'))
      with open(d, 'rt') as f: sessions = f.read().split()
      return [File(k) for k in self.metadata if k in sessions]
    
    if protocol in ('traindev_clean')
      d = resource_filename(__name__, os.path.join('data', 'traindev_clean.txt'))
      with open(d, 'rt') as f: sessions = f.read().split()
      return [File(k) for k in self.metadata if k in sessions]
    
    if protocol in ('traindev_all',):
      d = resource_filename(__name__, os.path.join('data', 'traindev_all.txt'))
      with open(d, 'rt') as f: sessions = f.read().split()
      return [File(k) for k in self.metadata if k in sessions]
    
    if protocol in ('test_clean')
      d = resource_filename(__name__, os.path.join('data', 'test_clean.txt'))
      with open(d, 'rt') as f: sessions = f.read().split()
      return [File(k) for k in self.metadata if k in sessions]
    
    if protocol in ('test_all',):
      d = resource_filename(__name__, os.path.join('data', 'test_all.txt'))
      with open(d, 'rt') as f: sessions = f.read().split()
      return [File(k) for k in self.metadata if k in sessions]

    return [File(k) for k in self.metadata]
