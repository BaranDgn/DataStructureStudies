# Deque

"""
class Deque

add()
addLeft()
addRight()

removeRight()
removeLeft()

isEmpty()
size()

"""


class Deque():

    def __init__(self):
        self.elements = []

    def addLeft(self, element):
        self.elements.insert(0, element)

    def addRight(self, element):
        self.elements.append(element)

    def removeLeft(self):
        return self.elements.pop(0)

    def removeRight(self):
        return self.elements.pop()

    def isEmpty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)

    def printingDeque(self):
        for i in self.elements:
            print(i)


myDeque = Deque()

myDeque.addLeft(10)
myDeque.addLeft(20)
myDeque.addLeft(30)

myDeque.addRight(40)
myDeque.addRight(50)

myDeque.removeLeft()
myDeque.removeRight()
myDeque.size()
myDeque.isEmpty()
myDeque.printingDeque()
