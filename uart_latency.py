import sys
import serial
import time
import threading
from pynput import keyboard


class UART:
    def __init__(self, port, interival = 1.0):
        self.stop = False
        self.interval = interval
        slef.port = port

    def message(self, msgs):
        self.messages = msgs

    def _loop(self):
        if self.stop == True:
            return
        threading.Timer(self.interval, self._loop, [self]).start()
        _loop_message()

    def _loop_message(self):

global_stop = False
t = 0

def nock_init(ser, mesg):
    if global_stop == True:
       return
    threading.Timer(1.0, nock_init, [ser, mesg]).start()
    loop_message(ser, mesg)

def port_open(port):
    return serial.Serial(port, 115200)

def loop_message(ser, mesg):
    global t
    t = time.perf_counter_ns()
    ser.write(mesg)

def print_usage():
    print(sys.argv[0], " need [port] [test strings]")

def on_press(key):
    print('{0} pressed'.format(key))
    return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print_usage()
        quit()
    ser = port_open(sys.argv[1])
    if ser.is_open == False:
        print(sys.argv[1], " open failed")
        quit()
    mesg = str(sys.argv[2] + '\n').encode('utf-8')
    print("loop string length", len(mesg))
    nock_init(ser, mesg)

    with keyboard.Listener(on_press = on_press) as listener:
        listener.join()
        global_stop = True
    while global_stop == False:
        line = ser.readline()
        print(line, "->", time.perf_counter_ns() - t, "ns")
