import time
import threading

class UART:
    def __init__(self, port, interval = 1.0):
        self.stop = False
        self.interval = interval
        self.port = port
        self.start = None
        self.messages = []
        self.index = None

    def message(self, msgs):
        for s in msgs:
            self.messages.append(str(s + '\n').encode('utf-8'))
        self.index = 0
        self._loop()

    def _loop(self):
        if self.stop == True:
            return
        threading.Timer(self.interval, self._loop, [self]).start()
        self._loop_message()

    def _loop_message(self):
        self.start = time.perf_counter_ns()
        self.port.write(self.messages
                [self.index])
        self.index += 1
        self.index %= len(self.messages)

    def _on_press(key):
        print('{0} pressed'.format(key))
        return False

    def loop(self):
        while self.stop == False:
            line = self.port.readline()
            print(line, "->", time.perf_counter_ns() - self.start, "ns")

