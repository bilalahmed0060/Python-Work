#-----------R-6.1---------------------

class Empty(Exception):
    pass

class ArrayStack:
    """LIFO Stack implementatino using a Python list as underlying storage."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

S = ArrayStack()
S.push(5)
S.push(3)
S.pop()
S.push(2)
S.push(8)
S.pop()
S.pop()
S.push(9)
S.push(1)
S.pop()
S.push(7)
S.push(6)
S.pop()
S.pop()
S.push(4)
S.pop()
S.pop()
print(S._data)
"""
Return   Values in the Stack
-        [5]
-        [5,3]
3        [5]
-        [5,2]
-        [5,2,8]
8        [5,2]
2        [5]
-        [5,9]
-        [5,9,1]
1        [5,9]
-        [5,9,7]
-        [5,9,7,6]
6        [5,9,7]
7        [5,9]
-        [5,9,4]
4        [5,9]
9        [5]
"""