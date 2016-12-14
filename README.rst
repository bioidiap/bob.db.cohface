.. vim: set fileencoding=utf-8 :
.. Wed  7 Dec 16:34:35 CET 2016

.. image:: http://img.shields.io/badge/docs-stable-yellow.png
   :target: http://pythonhosted.org/bob.db.cohface/index.html
.. image:: http://img.shields.io/badge/docs-latest-orange.png
   :target: https://www.idiap.ch/software/bob/docs/latest/bob/bob.db.cohface/master/index.html
.. image:: https://gitlab.idiap.ch/bob/bob.db.cohface/badges/v1.0.0/build.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.cohface/commits/v1.0.0
.. image:: https://img.shields.io/badge/gitlab-project-0000c0.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.cohface
.. image:: http://img.shields.io/pypi/v/bob.db.cohface.png
   :target: https://pypi.python.org/pypi/bob.db.cohface
.. image:: http://img.shields.io/pypi/dm/bob.db.cohface.png
   :target: https://pypi.python.org/pypi/bob.db.cohface


=====================================
 COHFACE Database Access API for Bob
=====================================

This package is part of the signal-processing and machine learning toolbox
Bob_. It contains an interface for the evaluation protocols of the `COHFACE
Database`_. Notice this package does not contain the raw data files from this
dataset, which need to be obtained through the link above.


Installation
------------

Follow our `installation`_ instructions. Then, using the Python interpreter
provided by the distribution, bootstrap and buildout this package::

  $ python bootstrap-buildout.py
  $ ./bin/buildout


Contact
-------

For questions or reporting issues to this software package, contact our
development `mailing list`_.


.. Place your references here:
.. _bob: https://www.idiap.ch/software/bob
.. _installation: https://www.idiap.ch/software/bob/install
.. _mailing list: https://www.idiap.ch/software/bob/discuss
.. _cohface database: https://www.idiap.ch/dataset/cohface
