#-------------project#1 stack------------
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
    def printStack(self):
        print('Stack of the registered patient ages ', end=' ')
        for data in self._data:
            print(data,end=' ')
        print('\n')

class SortStack:
    """LIFO Stack implementatino using a Python list as underlying storage."""

    def __init__(self,stack):
        self._data = []
        self.temStack = stack
        # while temporary stack is not
        while self.temStack.is_empty() == False:

            # pop out the first element
            tmp = self.temStack.top()
            self.temStack.pop()

            # while temporary stack is not
            # empty and top of stack is
            # less than temp
            while (self.is_empty() == False and
                   int(self._data[-1]) < int(tmp)):
                # pop from temporary stack and
                # push it to the input stack
                self.temStack.push(self._data[-1])
                self.pop()

            # push temp in tempory of stack
            self.push(tmp)

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    # Function to pop an
    # item from stack
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def printStack(self):
        print('the candidat stack ',end=' ')
        for data in self._data:
            print(data, end=' ')
        print('\n')




S = ArrayStack()
S.push(30)
S.push(19)
S.push(65)
S.push(42)
S.push(16)
S.push(73)
S.push(25)
S.push(94)
S.push(53)
S.printStack()
S1 = SortStack(S)
S1.printStack()
