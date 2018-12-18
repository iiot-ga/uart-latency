#!/usr/bin/env python
"""
uart-latency
-------------------------------------------------------------------------

Gauge looped UART port latancy
"""

if __name__ == '__main__':  # noqa
    import argparse
    parser = argparse.ArgumentParser(
            description='Simple Serial gauge latency that include network(TCP/IP) path, if.',
            epilog="""\
NOTE: the measure is not ignore reciveing time that more characters is more time.
""")
    parser.add_argument(
            'SERIALPORT',
            help="serial port name")

    parser.add_argument(
            '-q', '--quiet',
            action='store_true',
            help='suppress non error messages',
            default=False)

    parser.add_argument(
            '--develop',
            action='store_true',
            help='Development mode, prints Python internals on errors',
            default=False)

    parser.add_argument(
            "--interval",
            type=float,
            help='between sent message interval, default: 1.0 sec',
            default=1.0)

    parser.add_argument(
            'MESSAGE',
            help='gauge loop-back tranmiting time of message',
            nargs='+')

    group = parser.add_argument_group('serial port')

    parser.add_argument(
            '-B', '--baudrate',
            type=int,
            nargs='?',
            help='set baud rate, default: %(default)s',
            default=9600)

    group.add_argument(
            "--parity",
            choices=['N', 'E', 'O', 'S', 'M'],
            type=lambda c: c.upper(),
            help="set parity, one of {N E O S M}, default: N",
            default='N')

    group.add_argument(
            '--bytesize',
            type=int,
            choices=range(5, 9),
            help="set data bits, one of {5,6,7,8}, default: 8",
            default=8)

    group.add_argument(
            '--stopbits',
            type=int,
            choices=[1, 2],
            help="set stop bits, one of {1,2}, default: 1",
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

    group = parser.add_argument_group('network settings')

    exclusive_group = group.add_mutually_exclusive_group()

    exclusive_group.add_argument(
            '-P', '--localport',
            type=int,
            help='local TCP port',
            default=7777)

    exclusive_group.add_argument(
            '-c', '--client',
            metavar='HOST:PORT',
            help='make the connection as a client, instead of running a server',
            default=False)

    args = parser.parse_args()

    if args.develop:
        print(args)

    # connect to serial port
    import serial
    import sys

    ser = serial.serial_for_url(args.SERIALPORT, do_not_open=True)
    ser.baudrate = args.baudrate
    ser.parity = args.parity
    ser.rtscts = args.rtscts
    ser.xonxoff = args.xonxoff
    ser.bytesize = args.bytesize
    ser.stopbits = args.stopbits

    if args.rts is not None:
        ser.rts = args.rts

    if args.dtr is not None:
        ser.dtr = args.dtr

    if not args.quiet:
        sys.stderr.write(
                '--- TCP/IP to Serial redirect on {p.name}  {p.baudrate},{p.bytesize},{p.parity},{p.stopbits} ---\n'
                '--- type Ctrl-C / BREAK to quit\n'.format(p=ser))

    try:
        ser.open()
    except serial.SerialException as e:
        sys.stderr.write('Could not open serial port {}: {}\n'.format(ser.name, e))
        sys.exit(1)

    import loop

    uart = loop.UART(ser, args.interval)
    uart.message(args.MESSAGE)
    uart.start()
    try:
        while True:
            uart.readline()
    except KeyboardInterrupt:
        uart.stop()

