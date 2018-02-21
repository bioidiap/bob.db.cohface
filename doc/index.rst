.. vim: set fileencoding=utf-8 :

.. _bob.db.cohface:

==================
 COHFACE Database
==================

Development
===========

This package can, optionally, automatically annotate the following key aspects
of the COHFACE dataset:

* Average heart-rate in beats-per-minute (BPM), using a custom peak detector
* Face bounding boxes, as detected by the default detector on
  :ref:`bob.ip.facedetect`

.. warning::

   Note this procedure is **outdated** by current metadata which is already
   shipped with the COHFACE dataset and this package. Only use it in case you
   know what you're doing and/or want to modify/re-evaluate this package's
   metadata.

   For it to work properly, you'll need to modify the method
   :py:meth:`bob.db.cohface.File.load_face_detection` to take it into account.
   As of today, it is set to load face detections from the files distributed
   with the COHFACE dataset.


The annotation procedure can be launched with the following command:

.. code-block:: sh

   $ bob_dbmanage.py cohface mkmeta


Each video, which is composed of a significant number of frames (hundreds),
takes about 5 minutes to get completely processed. If are at Idiap, you can
launch the job on the SGE queue using the following command-line:

.. code-block:: sh

   $ jman sub -q q1d --io-big -t 160 `which bob_dbmanage.py` cohface mkmeta


API
===

.. automodule:: bob.db.cohface
