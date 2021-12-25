#-----------R-7.2-------------

class Empty(Exception):
    pass


class LinkedStack:
    """LIFO Stack implementatino using a singly linked list for storage"""

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        cur = self._head
        while cur is not None:
            yield cur._element
            cur = cur._next

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def printList(self):
        """Add a node in the end of the linked list."""
        if self._head is not None:
            temp = self._head
            while temp is not None:
                print(temp._element, end=" ")
                temp = temp._next

        else:
            print("List is empty")
        print()


def concat_singly_linked_stack(base, append):
    # base = copy.deepcopy(base)
    # append = copy.deepcopy(append)

    base_last = None
    cur = base._head
    while True:  # Need to traverse whole list since LinkedStack does not keep its last node.
        if cur._next is None:
            base_last = cur
            break
        cur = cur._next
    base_last._next = append._head
    base._size += append._size
    return base


L = LinkedStack()
L.push(5)
L.push(4)
L.push(3)
print("List L :",end=' ')
L.printList()

M = LinkedStack()
M.push(3)
M.push(2)
M.push(1)
print("List M :",end=' ')
M.printList()

concat_list = concat_singly_linked_stack(L, M)
print("Combined list :",end=' ')
concat_list.printList()
# print([i for i in concat_list])