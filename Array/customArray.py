# declaring default capacity
DEFAULT_CAPACITY = 53

class CustomArray():
    def __init__(self, capacity = DEFAULT_CAPACITY):
        self.capacity = capacity
        self.array = [None] * capacity
        self.length = 0

    def __resize(self, newCapacity):
        if newCapacity == self.capacity:
            return

        newArray = [None] * newCapacity
        for i in range(self.length):
            newArray[i] = self.array[i]
        self.array = newArray
        self.capacity = newCapacity

    def __grow(self):
        self.__resize(self.capacity * 2)

    def __shrink(self):
        if self.capacity / 2 < self.length:
            return
        self.__resize(int(self.capacity / 2))

    def push(self, element):
        if self.length == self.capacity:
            self.__grow()
        self.array[self.length] = element
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise Exception("Array is empty")
        element = self.array[self.length - 1]
        self.length -= 1

        if self.length < self.capacity / 4:
            self.__shrink()
        return element

    def insert(self, index, element):
        if index < 0 or index > self.length:
            raise Exception("Index out of bounds")

        if self.length == self.capacity:
            self.__grow()

        for i in range(self.length, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Index out of bounds")

        element = self.array[index]
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.length -= 1

        if self.length < self.capacity / 4:
            self.__shrink()
        return element

    def get(self, index):
        if index < 0 or index >= self.length:
            raise Exception("Index out of bounds")
        return self.array[index]

    def set(self, index, element):
        if index < 0 or index >= self.length:
            raise Exception("Index out of bounds")
        self.array[index] = element

    def index_of(self, element):
        for i in range(self.length):
            if self.array[i] == element:
                return i
        return -1

    def contains(self, element):
        return self.index_of(element) != -1

    def to_array(self):
        return self.array[:self.length]

customArray = CustomArray()
customArray.push(5)
customArray.push(2)
customArray.push(3)

print(customArray.to_array())