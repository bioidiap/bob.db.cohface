.. vim: set fileencoding=utf-8 :
.. Andre Anjos <andre.anjos@idiap.ch>
.. Tue 20 Oct 2015 15:52:00 CEST

====================================
 COHFACE Database Interface for Bob
====================================

This package contains an interface for the COHFACE dataset, which is useful
for measuring the performance of heart-rate estimation algorithms from webcam
videos.

This package heavily depends on bob_, so if you use this package and/or its results, please cite the following publication::

    @inproceedings{Anjos_ACMMM_2012,
        author = {A. Anjos AND L. El Shafey AND R. Wallace AND M. G\"unther AND C. McCool AND S. Marcel},
        title = {Bob: a free signal processing and machine learning toolbox for researchers},
        year = {2012},
        month = oct,
        booktitle = {20th ACM Conference on Multimedia Systems (ACMMM), Nara, Japan},
        publisher = {ACM Press},
    }

    
Installation
------------

To install the package, git-clone it or download the zip archive, open a terminal and run:

  .. code:: bash 
     
     $ cd bob.rppg.base
     $ python bootstrap-buildout.py
     $ ./bin/buildout


For bob_ (and hence this package) to be able to work properly, some dependent packages are required to be installed.
Please make sure that you have read the `Dependencies <https://github.com/idiap/bob/wiki/Dependencies>`_ for your operating system.
In particular, this package requires OpenCV (version 2.4.10) to be installed. If you have a different version (i.e 
version 3), the code might need some editing, see full documentation for details.

Dependencies
============

This package makes use of the following important external dependencies:

  * bob.ip.facedetect_: For automatically detecting faces using a boosted
    classifier based on LBPs


Usage
-----

You can read videos and sensor information out of the database using the
provided API.


Annotations
===========

This package can, optionally, *automatically* annotate the following key
aspects of the Mahnob HCI-Tagging dataset:

  * Average heart-rate in beats-per-minute (BPM), using the Pam-Tompkins
    algorithm as implemented by `mne`_.
  * Face bounding boxes, as detected by the default detector on
    `bob.ip.facedetect`_.


The annotation procedure can be launched with the following command::

  $ ./bin/bob_dbmanage.py cohface mkmeta


Each video, which is composed of a significant number of frames (hundreds),
takes about 5 minutes to get completely processed. If are at Idiap, you can
launch the job on the SGE queue using the following command-line::

  $ ./bin/jman sub -q q1d --io-big -t 3490 `pwd`/bin/bob_dbmanage.py cohface mkmeta


.. Your references go here

.. _bob: https://www.idiap.ch/software/bob
.. _mahnob hci-tagging dataset: http://mahnob-db.eu/hci-tagging/
.. _bob.ip.facedetect: https://pypi.python.org/pypi/bob.ip.facedetect
.. _mne: https://pypi.python.org/pypi/mne
