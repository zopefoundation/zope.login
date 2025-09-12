=========
 Changes
=========

4.0 (2025-09-12)
================

- Replace ``pkg_resources`` namespace with PEP 420 native namespace.


3.1 (2025-02-14)
================

- Add support for Python 3.12, 3.13.

- Drop support for Python 3.7, 3.8.


3.0 (2023-08-23)
================

- Drop support for Python 2.7, 3.5, 3.6.

- Add support for Python 3.11.


2.2 (2022-04-29)
================

- Add support for Python 3.7, 3.8, 3.9, 3.10.


2.1.0 (2017-09-01)
==================

- Add support for Python 3.5 and 3.6.

- Drop support for Python 2.6 and 3.3.

- Host documentation at https://zopelogin.readthedocs.io/

2.0.0 (2014-12-24)
==================

- Add support for PyPy and PyPy3.

- Add support for Python 3.4.

- Add support for testing on Travis.

- Add support for Python 3.3.

- Replace deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Drop support for Python 2.4 and 2.5.


1.0.0 (2009-12-31)
==================

- Extracted BasicAuthAdapter and FTPAuth adapters from zope.publisher. They
  should have never gone into that package in the first place.
