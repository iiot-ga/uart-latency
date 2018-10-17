"""
loop.py
-------------------------------------------------------------------------

Used Python3.7 API that's time.perf_counter_ns(), so lock python version
"""
import sys
assert sys.version_info >= (3,7)

import time
import threading

class UART(threading.Thread):
    def __init__(self, port, interval = 1.0):
        threading.Thread.__init__(self)
        self.runable = True
        self.interval = interval
        self.port = port
        self.tx_time = None
        self.tx_duty = None
        self.messages = []
        self.index = None

    def message(self, msgs):
        for s in msgs:
            m = str(s + '\n').encode('utf-8')
            self.messages.append(m)
            print(m, "(", len(m), ")")
        self.index = 0

    def run(self):
        while self.runable:
            self.tx_time = time.perf_counter_ns()
            self.port.write(self.messages[self.index])
            self.tx_duty = time.perf_counter_ns() - self.tx_time
            self.index += 1
            self.index %= len(self.messages)
            time.sleep(self.interval)

    def readline(self):
        if self.runable:
            line = self.port.readline()
            print("%9d ns (%7d ns)->%s" % (time.perf_counter_ns() - self.tx_time,
                    self.tx_duty, line))

    def stop(self):
        self.runable = False
