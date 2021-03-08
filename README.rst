======
TWSEIA
======

.. image:: https://travis-ci.com/slee124565/twseia.svg?branch=main
   :target: https://travis-ci.com/slee124565/twseia

.. image:: https://coveralls.io/repos/github/slee124565/twseia/badge.svg?branch=main
   :target: https://coveralls.io/github/slee124565/twseia?branch=main

.. image:: https://img.shields.io/hexpm/l/plug.svg
   :target: https://github.com/slee124565/twseia/blob/main/LICENSE

.. image:: https://img.shields.io/pypi/v/twseia.svg
   :target: https://pypi.org/project/twseia

A Taiwan Smart Energy Industry Association (TaiSEIA) Protocol Python Library.

Example
-------

Read POWER state from TaiSEIA device::

    import twseia
    sa = twseia.SmartApplication()
    service_id = 0
    r = sa.read_state(service_id)

Write POWER command to TaiSEIA device::

    import twseia
    sa = twseia.SmartApplication()
    service_id = 0
    POWER_ON = 1
    r = sa.write_state(service_id, POWER_ON)
    print(r.to_json())

Web resources
-------------

* **Documentation**: https://twseia.readthedocs.io/
* Source code on **GitHub**: https://github.com/slee124565/twseia
* Python package index (PyPI) with download: https://pypi.org/project/twseia/

Features
--------
TWSEIA is an easy-to-use Python module for talking to instruments (slaves)
from a computer (master) using the TaiSEIA protocol, and is intended to be running on the master.
The only dependence is the pySerial module (also pure Python).

There are convenience functions to handle floats, strings and long integers
(in different byte orders).

It is open source, and has the Apache License, Version 2.0.

Tested with Python 3.8 and 3.9.
