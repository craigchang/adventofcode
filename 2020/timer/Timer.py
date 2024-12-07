import time

class Timer:
    def __init__(self):
        self._start = 0
        self._end = 0

    def start(self):
        self._start = time.time()
    
    def end(self):
        self._end = time.time()

    def printTimeElapsed(self):
        print("%.2f"%((self._end-self._start)*1000), "ms") 

