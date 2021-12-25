#-----------R-6.7-------------

class Empty(Exception):
    pass

class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):

        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):

        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
Q = ArrayQueue()
Q.enqueue(5)
Q.enqueue(3)
Q.dequeue()
Q.enqueue(2)
Q.enqueue(8)
Q.dequeue()
Q.dequeue()
Q.enqueue(9)
Q.enqueue(1)
Q.dequeue()
Q.enqueue(7)
Q.enqueue(6)
Q.dequeue()
Q.dequeue()
Q.enqueue(4)
Q.dequeue()
Q.dequeue()
print(Q._data)

"""
Return   Values in the Stack
-        [5]
-        [5,3]
5        [3]
-        [3,2]
-        [3,2,8]
3        [2,8]
2        [8]
-        [8,9]
-        [8,9,1]
8        [9,1]
-        [9,1,7]
-        [9,1,7,6]
9        [1,7,6]
1        [7,6]
-        [7,6,4]
7        [6,4]
6        [4]

"""


