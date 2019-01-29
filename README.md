# uart-latency
Gauge loop-back serial port latency, It also suuprts RFC2217.
## Getting Started
Please prepare a UART device or RFC2217 remove device for testing. And python3.7 because used 'time.perf_counter_ns()' of Pythond 3.7 API.
### Prerequisites
It's better used "venv" for **virtual environments**
```
git clone https://github.com/iiot-ga/uart-latency.git
python3.7 -m venv uart-latency
cd uart-latency
source bin/activate
pip install pyserial
```
### Listing local UART ports (Support on both Linux and windows)
```
python -m serial.tools.list_ports
```
### Help
```
python uart-latency --help

(uart-latency) roger@roger-on-liteon-ia:~/uart-latency$ python uart_latency.py --help
usage: uart_latency.py [-h] [-q] [--develop] [--interval INTERVAL]
                       [--parity {N,E,O,S,M}] [--rtscts] [--xonxoff]
                       [--rts RTS] [--dtr DTR] [-P LOCALPORT | -c HOST:PORT]
                       SERIALPORT [BAUDRATE] MESSAGE [MESSAGE ...]

Simple Serial gauge latency that include network(TCP/IP) path, if.

positional arguments:
  SERIALPORT            serial port name
  BAUDRATE              set baud rate, default: 9600
  MESSAGE               gauge loop-back tranmiting time of message

optional arguments:
  -h, --help            show this help message and exit
  -q, --quiet           suppress non error messages
  --develop             Development mode, prints Python internals on errors
  --interval INTERVAL   between sent message interval, default: 1.0 sec

serial port:
  --parity {N,E,O,S,M}  set parity, one of {N E O S M}, default: N
  --rtscts              enable RTS/CTS flow control (default off)
  --xonxoff             enable software flow control (default off)
  --rts RTS             set initial RTS line state (possible values: 0, 1)
  --dtr DTR             set initial DTR line state (possible values: 0, 1)

network settings:
  -P LOCALPORT, --localport LOCALPORT
                        local TCP port
  -c HOST:PORT, --client HOST:PORT
                        make the connection as a client, instead of running a
                        server

NOTE: the measure is not ignore reciveing time that more characters is more
time.
```
### Example
```
python uart_latency.py --develop  --interval 0.5 /dev/ttyUSB0 115200 testwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww t te tes test
```

### TEST
