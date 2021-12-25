#=============P-9.53==============

from datetime import datetime
class PQueue:
    def __init__(self, size):
        self.q = []
        self.rear = -1
        self.front = -1
        self.limit = size


    def enQueue(self, element):
        size = len(self.q)
        if self.isEmpty():
            self.front = 0
            self.rear = 0
            self.q.append(element)
        elif self.isFull():
            print('Over flow!')
        else:
            self.rear += 1
            self.q.append(element)
            for i in range((size // 2) - 1, -1, -1):
                heapify(self.q, size, i)

    def deQueue(self, element):
        size = len(self.q)
        i = 0
        if self.isEmpty():
            print('Under flow!')
        else:
            if self.front == self.rear:
                self.rear = self.front = -1
                self.q = []
            else:
                for i in range(0, size):
                    if element == self.q[i]:
                        break
                self.q[i], self.q[size - 1] = self.q[size - 1], self.q[i]
                self.front += 1
                self.q.remove(size - 1)

                for i in range((len(self.q) // 2) - 1, -1, -1):
                    heapify(self.q, len(self.q), i)

    def isEmpty(self):
        return True if self.rear == -1 and self.front == -1 else False

    def isFull(self):
        return True if len(self.q) == self.limit else False

    def printQueue(self):
        print(self.q, ', rear: ', self.rear, ', front: ', self.front)


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        # swap in place
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify the root.
        heapify(arr, n, largest)


def heapSortNotInPlace(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        temp = arr
        heapify(temp, n, i)
        arr = temp

    for i in range(n-1, 0, -1):
        # swap
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        heapify(arr, i, 0)

    return arr


def heapSortInPlace(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


if __name__ == '__main__':
    nums = [x for x in reversed(range(1, 1000))]
    size = len(nums)

    queue_1 = PQueue(size)
    [queue_1.enQueue(x) for x in nums]
    print('Priority Queue 1 : ', end='')
    queue_1.printQueue()
    q_1 = queue_1.q
    print('Applying heapSortInPlace() on queue_1')
    start1 = datetime.now()
    q_1 = heapSortInPlace(q_1)
    stop1 = datetime.now()
    print('Sorted Priority Queue 1 : ', end='')
    queue_1.printQueue()

    print('\n\n')

    queue_2 = PQueue(size)
    [queue_2.enQueue(x) for x in nums]
    print('Priority Queue 2 : ', end='')
    queue_2.printQueue()
    q_2 = queue_2.q
    print('Applying heapSortInNotPlace() on queue_2')
    start2 = datetime.now()
    q_2 = heapSortNotInPlace(q_2)
    stop2 = datetime.now()
    print('Sorted Priority Queue 2 : ', end='')
    queue_2.printQueue()


    print('\n\n')
    
    print('Results: \n\
    heapSortInPlace()    execution time: {0}\n\
    heapSortInNotPlace() execution time: {1}\n'.format(stop1-start1, stop2-start2))
