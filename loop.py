import time
import threading
from pynput import keyboard


class UART:
    def __init__(self, port, interval = 1.0):
        self.stop = False
        self.interval = interval
        self.port = port
        self.start = None
        self.messages = None

    def message(self, msgs):
        self.messages = msgs

    def _loop(self):
        if self.stop == True:
            return
        threading.Timer(self.interval, self._loop, [self]).start()
        _loop_message()

    def _loop_message(self):
        self.start = time.perf_counter_ns()
        self.port.write(mesg)

    def _on_press(key):
        print('{0} pressed'.format(key))
        return False

    def loop(self):
        while self.stop == False:
            line = self.port.readline()
            print(line, "->", time.perf_counter_ns() - self.start, "ns")

