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


.. image:: https://img.shields.io/readthedocs/twseia
   :target: https://twseia.readthedocs.io/

A Taiwan Smart Energy Industry Association (TaiSEIA) Protocol Python Library.

Example
-------

Simple read and switch TaiSEIA device power ON/OFF state.::

    import sys
    import serial
    import twseia

    ser = serial.serial_for_url('/dev/ttyUSB0', do_not_open=True)
    ser.baudrate = 9600
    ser.bytesize = 8
    ser.parity = 'N'
    ser.stopbits = 1

    # TaiSEIA spec. constants
    SA_TYPE_ID = 4  # Dehumidifier
    POWER_SERVICE_ID = 0x00
    POWER_ON = 1
    POWER_OFF = 0

    # read device current power state
    read_cmd = twseia.create_read_state_cmd(SA_TYPE_ID, POWER_SERVICE_ID)
    ser.write(bytearray(read_cmd))
    buffer = []
    while not 0 < len(buffer) == buffer[0]:
        recv = ser.read()
        buffer += list(recv)
    response = twseia.parsing_read_state_response(SA_TYPE_ID, buffer)
    sys.stderr.write('read dev power state {}\n'.format(
        'ON' if response.get('value') == POWER_ON else 'OFF'
    ))

    # write power cmd to device
    cmd_value = POWER_OFF if response.get('value') == POWER_ON else POWER_ON
    write_cmd = twseia.create_write_state_cmd_from_txt(
        SA_TYPE_ID, 'power', cmd_value
    )
    sys.stderr.write('write dev power state {}\n'.format(
        'ON' if cmd_value == POWER_ON else 'OFF'
    ))
    ser.write(bytearray(write_cmd))
    buffer = []
    while not 0 < len(buffer) == buffer[0]:
        recv = ser.read()
        buffer += list(recv)
    response = twseia.parsing_read_state_response(SA_TYPE_ID, buffer)
    sys.stderr.write('dev report power state {}\n'.format(
        'ON' if response.get('value') == POWER_ON else 'OFF'
    ))

Web resources
-------------

* Taiwan Smart Energy Industry Association (TaiSEIA): http://www.taiseia.org.tw/
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
