#QUEUE

"""
class Queue
enqueue(element)
dequeue()
size()
isEmpty()

"""

class Queue():
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def enqueue(self, element):
        self.elements.insert(0, element)

    def dequeue(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def printing(self):
        for x in self.elements:
            print(x)

myQueue = Queue()

myQueue.enqueue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)
myQueue.enqueue(40)

print(myQueue)
print(myQueue.enqueue(50))
myQueue.printing()
print(myQueue.dequeue())

