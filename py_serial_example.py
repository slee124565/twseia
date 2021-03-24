import sys
import serial
import twseia

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Simple Serial to TaiSEIA home application example.',
        epilog="""\
NOTE: no security measures are implemented. 

Only one connection at once is supported. When the connection is terminated
it waits for the next connect.
""")

    parser.add_argument(
        'SERIALPORT',
        help="serial port name")

    parser.add_argument(
        'BAUDRATE',
        type=int,
        nargs='?',
        help='set baud rate, default: %(default)s',
        default=9600)

    group = parser.add_argument_group('serial port')

    group.add_argument(
        "--bytesize",
        choices=[5, 6, 7, 8],
        type=int,
        help="set bytesize, one of {5 6 7 8}, default: 8",
        default=8)

    group.add_argument(
        "--parity",
        choices=['N', 'E', 'O', 'S', 'M'],
        type=lambda c: c.upper(),
        help="set parity, one of {N E O S M}, default: N",
        default='N')

    group.add_argument(
        "--stopbits",
        choices=[1, 1.5, 2],
        type=float,
        help="set stopbits, one of {1 1.5 2}, default: 1",
        default=1)

    group.add_argument(
        '--rtscts',
        action='store_true',
        help='enable RTS/CTS flow control (default off)',
        default=False)

    group.add_argument(
        '--xonxoff',
        action='store_true',
        help='enable software flow control (default off)',
        default=False)

    group.add_argument(
        '--rts',
        type=int,
        help='set initial RTS line state (possible values: 0, 1)',
        default=None)

    group.add_argument(
        '--dtr',
        type=int,
        help='set initial DTR line state (possible values: 0, 1)',
        default=None)

    args = parser.parse_args()

    # connect to serial port
    ser = serial.serial_for_url(args.SERIALPORT, do_not_open=True)
    ser.baudrate = args.BAUDRATE
    ser.bytesize = args.bytesize
    ser.parity = args.parity
    ser.stopbits = args.stopbits
    ser.rtscts = args.rtscts
    ser.xonxoff = args.xonxoff

    if args.rts is not None:
        ser.rts = args.rts

    if args.dtr is not None:
        ser.dtr = args.dtr

    try:
        ser.open()
    except serial.SerialException as e:
        sys.stderr.write('Could not open serial port {}: {}\n'.format(ser.description, e))
        sys.exit(1)

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
