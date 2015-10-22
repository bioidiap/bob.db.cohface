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


  def objects(self):
    """Returns a list of unique :py:class:`.File` objects for the specific
    query by the user.

    Returns: A list of :py:class:`.File` objects.
    """

    return [File(k) for k in self.metadata]
