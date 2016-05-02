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

  def objects(self, protocol='all', subset=None):
    """Returns a list of unique :py:class:`.File` objects for the specific
    query by the user.

    Parameters:
      
      protocol (str, optional): If set, it should be either 'clean', 'natural' or 'all'.
        All, which is the default, considers all the illumination conditions 
        whereas clean retrieves only sequences where the spot in on and natural the ones
        with daylight illumination.

      subset (str, optional): If set, it could be either 'train', 'dev' or 'test'
        or a combination of them (i.e. a list). If not set (default), 
        the files from all these sets are retrieved, according to the protocol.

    Returns: A list of :py:class:`.File` objects.
    """
    files = []

    # clean protocol -> face is illuminated with a spot
    if protocol in ('clean'):

      if 'None' in subset:
        d = resource_filename(__name__, os.path.join('protocols/clean', 'all.txt'))
        with open(d, 'rt') as f: sessions = f.read().split()
        files += [File(k) for k in self.metadata if k in sessions]
        return files
      else:
        if 'train' in subset:
          d = resource_filename(__name__, os.path.join('protocols/clean', 'train.txt'))
          with open(d, 'rt') as f: sessions = f.read().split()
          files += [File(k) for k in self.metadata if k in sessions]
        if 'dev' in subset:
          d = resource_filename(__name__, os.path.join('protocols/clean', 'dev.txt'))
          with open(d, 'rt') as f: sessions = f.read().split()
          files += [File(k) for k in self.metadata if k in sessions]
        if 'test' in subset:
          d = resource_filename(__name__, os.path.join('protocols/clean', 'test.txt'))
          with open(d, 'rt') as f: sessions = f.read().split()
          files += [File(k) for k in self.metadata if k in sessions]
        
        return files

    # natural protocol -> no specific illumination (daylight)
    if protocol in ('natural'):

      if 'None' in subset:
        d = resource_filename(__name__, os.path.join('protocols/natural', 'all.txt'))
        with open(d, 'rt') as f: sessions = f.read().split()
        files += [File(k) for k in self.metadata if k in sessions]
        return files
      else:
        if 'train' in subset:
          d = resource_filename(__name__, os.path.join('protocols/natural', 'train.txt'))
          with open(d, 'rt') as f: sessions = f.read().split()
          files += [File(k) for k in self.metadata if k in sessions]
        if 'dev' in subset:
          d = resource_filename(__name__, os.path.join('protocols/natural', 'dev.txt'))
          with open(d, 'rt') as f: sessions = f.read().split()
          files += [File(k) for k in self.metadata if k in sessions]
        if 'test' in subset:
          d = resource_filename(__name__, os.path.join('protocols/natural', 'test.txt'))
          with open(d, 'rt') as f: sessions = f.read().split()
          files += [File(k) for k in self.metadata if k in sessions]
        
        return files


    # protocol with both conditions, spot + natural illumination (default)
    if protocol in ('all'):
    
      if 'None' in subset:
        d = resource_filename(__name__, os.path.join('protocols/all', 'all.txt'))
        with open(d, 'rt') as f: sessions = f.read().split()
        files += [File(k) for k in self.metadata if k in sessions]
        return files
      else:
        if 'train' in subset:
          d = resource_filename(__name__, os.path.join('protocols/all', 'train.txt'))
          with open(d, 'rt') as f: sessions = f.read().split()
          files += [File(k) for k in self.metadata if k in sessions]
        if 'dev' in subset:
          d = resource_filename(__name__, os.path.join('protocols/all', 'dev.txt'))
          with open(d, 'rt') as f: sessions = f.read().split()
          files += [File(k) for k in self.metadata if k in sessions]
        if 'test' in subset:
          d = resource_filename(__name__, os.path.join('protocols/all', 'test.txt'))
          with open(d, 'rt') as f: sessions = f.read().split()
          files += [File(k) for k in self.metadata if k in sessions]

      return files
