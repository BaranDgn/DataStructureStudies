# STACK INTERVIEW QUESTION


"""
Implement a last-in-first-out(LIFO) stack using only two queues.
The Implemented stack should support all the functions of a normal stack
(push, top, pop, and empty)

Implement the MyStack class:
    void push(int x) Pushes element x to the top of the stack
    int pop() Removes the element on the top the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() returns true if the stack is empty false otherwise

Notes:
    You must use only standard operations if a queue, which means that only push to back, peek/pop from front,
    size and is empty operations are valid.
    Depending on your language, the queue may not be supported natively, You may simulate a queue using a list ıf deque(double-ended queue)
    as long as you use only a queue's standard operations.

    EXAMPLE 1:
    Inout
    ["MyStack","push", "push", "top", "pop", "empty"]
    [[],[1],[2],[],[],[]]
    Output:
    [null,null,null,2,2,false]

    Explanation:
    MyStack mystack = new MyStack()
    mystack.push(1);
    mystack.push(2);
    mystack.top(); //return 2
    mystack.pop(); // return 2
    mystack.empty(); // return False
"""

# Stack i Queue ile yapma
# Stack te zaman complexity ekleme O(1), cıkarma O(1) olur.
# fakat asagıdaki yontemde zaman complexity ekleme O(1) iken cıkartma O(n) olacak
# cunku Queue kullanarak stack yapmak istedigimizde, ekleme islemi aynı oldugu icin bir sorun yaratmazken
# cıkarma isleminde ilk sıradaki elemanı son sıraya alarak stacke uygun bir cıkarma yapabilmek için.
# bu da bize O(n) zamanı olusturdu.

# 10 20 30

# Top içinde queue yu ters ten yazdırıp zaman complexity i arttırmamak icin
# Deque kullanarak da yapılabilir.
from collections import deque
from queue import Queue

class MyStack:
    def __init__(self):
        self.myQueue = deque()

    def push(self, x: int) -> None:
        self.myQueue.append(x)

    def pop(self):
        for i in range(0,len(self.myQueue)-1):
            self.myQueue.append(self.myQueue.popleft())
        return self.myQueue.popleft()

    def top(self) -> int:
        return self.myQueue[-1]

    def empty(self):
        return len(self.myQueue) == 0

obj = MyStack()
obj.push(10)
obj.push(20)
obj.push(30)
print(obj.top())
print(obj.empty())
print(obj.pop())

"""
class MyStackWithQueue:

    def __init__(self):
        self.myQueue = Queue()

    def push(self, item):
        self.myQueue.append(item)

    def pop(self):
        reverseQueue = Queue()
        print(self.myQueue)
        for i in range(0, len(self.myQueue) - 1):
            reverseQueue += self.myQueue.pop()
        print(reverseQueue)
        print(self.myQueue)
        return reverseQueue.pop()

    def top(self):
        return self.myQueue[-1]

    def size(self):
        return len(self.myQueue)

    def isEmpty(self):
        return self.myQueue == 0


myStackWithQueue = MyStackWithQueue()
myStackWithQueue.push(10)
myStackWithQueue.push(20)
myStackWithQueue.push(30)

print(myStackWithQueue.top())
print(myStackWithQueue.size())
print(myStackWithQueue.isEmpty())

print(myStackWithQueue.pop())
"""

# By using List
class MyStackWithList:

    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        elements2 = []
        for i in range(0, len(self.elements)):
            x = self.elements.pop()
            elements2.append(x)
        print(elements2)
        elements2.pop()
        print(self.elements)
        print(elements2)

    def top(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.elements == []

    def printingQueue(self):
        print(self.elements)


"""
myStackWithList = MyStackWithList()
myStackWithList.push(10)
myStackWithList.push(20)
myStackWithList.push(30)
myStackWithList.push(40)
print(myStackWithList.top())
print(myStackWithList.size())
myStackWithList.printingQueue()
myStackWithList.pop()
"""
"""
stack -- 10 20 30 
pop -- 30 -
queue -- 10 20 30
pop -- 10  
"""
