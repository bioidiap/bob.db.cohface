#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Tue 20 Oct 2015 16:33:32 CEST

import os
import collections
import pkg_resources

import bob.io.base

from . import utils

class File(object):
  """ Generic file container for COHFACE files


  Parameters:

    stem (str): The stem of the files for a particular session

  """

  def __init__(self, stem):

    self.stem = stem


  def __repr__(self):
    return "File('%s')" % self.stem


  def default_extension(self):
      return '.hdf5'


  def make_path(self, directory=None, extension=None):
    """Wraps this files' filename so that a complete path is formed

    Keyword parameters:

    directory
      An optional directory name that will be prefixed to the returned result.

    extension
      An optional extension that will be suffixed to the returned filename. The
      extension normally includes the leading ``.`` character as in ``.png`` or
      ``.bmp``. If not specified the default extension for the original file in
      the database will be used

    Returns a string containing the newly generated file path.
    """

    return os.path.join(
            directory or '',
            self.stem + (extension or self.default_extension()),
            )


  def load_video(self, directory):
    """Loads the colored video file associated to this object

    Keyword parameters:

    directory
      A directory name that will be prefixed to the returned result.

    """

    path = os.path.join(directory, self.stem + '.avi')
    return bob.io.video.reader(path)


  def estimate_heartrate_in_bpm(self, directory):
    """Estimates the person's heart rate using the ECG sensor data

    Keyword parameters:

      directory
        A directory name that leads to the location the database is installed
        on the local disk

    """

    from .utils import estimate_average_heartrate

    f = self.load_hdf5(directory)

    #avg_hr, peaks = estimate_average_heartrate(f.get('pulse'),
    avg_hr, peaks = estimate_average_heartrate(f.get('pulse'),
        float(f.get_attribute('sample-rate-hz')))
    return avg_hr


  def load_heart_rate_in_bpm(self):
    """Loads the heart-rate from locally stored files if they exist, fails
    gracefully otherwise, returning `None`"""

    data_dir = pkg_resources.resource_filename(__name__, 'data')
    path = self.make_path(data_dir, '.hdf5')

    if os.path.exists(path):
      f = bob.io.base.HDF5File(path)
      return f.get('heartrate')

    return None


  def load_drmf_keypoints(self):
    """Loads the 66-keypoints coming from the Discriminative Response Map
    Fitting (DRMF) landmark detector.

    Reference: http://ibug.doc.ic.ac.uk/resources/drmf-matlab-code-cvpr-2013/.

    The code was written for Matlab. Data for the first frame of the colour
    video of this object was loaded on a compatible Matlab framework and the
    keypoints extracted taking as basis the currently available face bounding
    box, enlarged by 7% (so the key-point detector performs reasonably well).
    The extracted keypoints were then merged into this database access package
    so they are easy to load from python.

    The points are in the form (y, x), as it is standard on Bob-based packages.
    """

    
    data_dir = pkg_resources.resource_filename(__name__, 'data')
    path = self.make_path(data_dir, '.hdf5')

    if os.path.exists(path):
      f = bob.io.base.HDF5File(path)
      return f.get('drmf_landmarks66')

    return None


  def load_hdf5(self, directory):
    """Loads the hdf5 file containing the sensor data


    Parameters:

    directory (str): A directory name that will be prefixed to the returned
      result.


    Returns:

      bob.io.base.HDF5File

    """

    path = os.path.join(directory, self.stem + '.hdf5')
    return bob.io.base.HDF5File(path)



  def metadata(self, directory):
    """Returns a dictionary with metadata about this session:


    Parameters:

    directory (str): A directory name that will be prefixed to the returned
      result.


    Returns:

    dict: Containing the following fields

      * birth-date (format: %d.%m.%Y)
      * client-id (format: %d)
      * illumination (str: lamp | natural)
      * sample-rate-hz (int: 256, always)
      * scale (str: "uV")
      * session (format: %d)

    These values are extracted from the HDF5 attributes
    """

    return self.load_hdf5(directory).get_attributes()


  def save(self, data, directory=None, extension='.hdf5'):
    """Saves the input data at the specified location and using the given
    extension.

    Keyword parameters:

    data
      The data blob to be saved (normally a :py:class:`numpy.ndarray`).

    directory
      If not empty or None, this directory is prefixed to the final file
      destination

    extension
      The extension of the filename - this will control the type of output and
      the codec for saving the input blob.
    """

    path = self.make_path(directory, extension)
    if not os.path.exists(os.path.dirname(path)):
      os.makedirs(os.path.dirname(path))
    bob.io.base.save(data, path)
