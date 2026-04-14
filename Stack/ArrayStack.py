class ArrayStack:
    def __init__(self, maxSize = 10):
        self.stack = [None] * maxSize
        self.top = -1
        self.maxSize = maxSize

    def push(self, data):
        if self.top >= self.maxSize - 1:
            raise Exception("Stack overflow")
        self.stack[self.top + 1] = data
        self.top += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack underflow")
        data = self.stack[self.top]
        self.top -= 1
        return data

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack underflow")
        return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

stack = ArrayStack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.peek()
stack.size()

print(stack.stack)