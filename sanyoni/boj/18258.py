import sys


class Queue:
    def __init__(self, initial_size: int):
        self.m_queue = [0] * initial_size
        self.m_front = 0
        self.m_back = -1

    def push(self, value):
        self.m_back += 1
        self.m_queue[self.m_back] = value

    def pop(self):
        if self.empty() == 1:
            return -1

        value = self.m_queue[self.m_front]
        self.m_front += 1
        return value

    def size(self):
        return (self.m_back - self.m_front) + 1

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size() == 0:
            return -1

        return self.m_queue[self.m_front]

    def back(self):
        if self.size() == 0:
            return -1

        return self.m_queue[self.m_back]


operations_counts = int(sys.stdin.readline().rstrip())

queue = Queue(operations_counts)

for i in range(operations_counts):
    operation_splitted = sys.stdin.readline().rstrip().split()

    if operation_splitted[0] == "push":
        queue.push(int(operation_splitted[1]))
    elif operation_splitted[0] == "pop":
        print(queue.pop())
    elif operation_splitted[0] == "size":
        print(queue.size())
    elif operation_splitted[0] == "empty":
        print(queue.empty())
    elif operation_splitted[0] == "front":
        print(queue.front())
    else:
        print(queue.back())
