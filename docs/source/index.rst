.. twseia documentation master file, created by
   sphinx-quickstart on Thu Mar  4 05:58:16 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to TWSEIA' documentation!
==================================

**TWSEIA** is a Python library for TaiSEIA device via serial port (via USB, RS485 or RS232).

-----

**Example**

 Read POWER state from TaiSEIA device::

     import twseia
     sa = twseia.SmartApplication()
     service_id = 0
     r = sa.read_state(service_id)
     print(r.to_json())

 Write POWER command to TaiSEIA device::

     import twseia
     sa = twseia.SmartApplication()
     service_id = 0
     POWER_ON = 1
     r = sa.write_state(service_id, POWER_ON)
     print(r.to_json())

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
