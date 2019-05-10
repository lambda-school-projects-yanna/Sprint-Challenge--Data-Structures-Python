class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.current > len(self.storage)-1:
            self.current = 0
        if None in self.storage:
            j = self.storage.index(None)
            self.storage[j] = item
        else:
            self.storage[self.current] = item
            self.current += 1
            
    def get(self):
        vals = [i for i in self.storage if i is not None]
        return vals