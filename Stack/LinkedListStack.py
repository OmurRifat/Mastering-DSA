class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self, maxSize = 10):
        self.top = None
        self.size = 0
        self.maxSize = maxSize

    def push(self, data):
        if self.size >= self.maxSize:
            raise Exception("Stack overflow")
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack underflow")
        data = self.top.value
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack underflow")
        return self.top.value

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size

    def print(self):
        current = self.top
        result = ''
        while current:
            result += str(current.value) + ' -> '
            current = current.next
        print(result)

stack = LinkedListStack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
print(stack.peek())
print(stack.size)
stack.print()