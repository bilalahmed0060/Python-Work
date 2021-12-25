#-----------R-7.5-------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

        # Function answer to Q2
        # Altered fucntion to count all nodes in list
    def print_list(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            print(cur.data,end=' ')
            cur = cur.next
            if cur == self.head:
                print()
                print('Count:', count)
                break


clist = CircularLinkedList()
clist.append(2)
clist.append(4)
clist.append(6)
clist.append(8)
clist.append(10)
#this method print the list and also count the nodes
clist.print_list()