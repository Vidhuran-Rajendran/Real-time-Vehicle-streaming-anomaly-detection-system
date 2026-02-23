from collections import deque

class SlidingWindow:
    def __init__(self,window_size=20):
        self.window = deque(maxlen=window_size)
        
    def updates(self, data):
        self.window.append(data)
        return list(self.window)