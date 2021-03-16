import sys


class Stack:
    def __init__(self):
        INITIAL_STACK_SIZE = 50

        self.m_top = -1
        self.m_stack = [0] * INITIAL_STACK_SIZE

    def push(self, value):
        self.m_top += 1

        if self.m_top >= len(self.m_stack):
            self.m_stack.append(value)
        else:
            self.m_stack[self.m_top] = value

    def pop(self):
        if self.m_top == -1:
            return -1

        value = self.m_stack[self.m_top]
        self.m_top -= 1
        return value

    def size(self):
        return self.m_top + 1

    def empty(self):
        if self.m_top == -1:
            return 1
        else:
            return 0

    def top(self):
        if self.m_top == -1:
            return -1

        return self.m_stack[self.m_top]


operation_count = int(sys.stdin.readline().rstrip())

stack = Stack()

for i in range(operation_count):
    operation_splitted = sys.stdin.readline().rstrip().split()
    if operation_splitted[0] == "push":
        stack.push(int(operation_splitted[1]))
    elif operation_splitted[0] == "pop":
        print(stack.pop())
    elif operation_splitted[0] == "size":
        print(stack.size())
    elif operation_splitted[0] == "empty":
        print(stack.empty())
    else:
        print(stack.top())