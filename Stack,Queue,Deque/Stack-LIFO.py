# STACK - LIFO

"""
Bir stack yaz sorusu gelebilir. Bu soruda bizden şu methodları da icinde olsun da denebilri.
Ornegin:
class Stack
push(item)
pop()
size()
isEmpty()
gibi mehodları olan bir stack yazmamız istenebilir.

!! Ayrıca burada stack yazarken direk baştan bir stack yazmak pek mümkün olmayabilir
en azından mülakat sartlarında. Bu nedenle asagıdaki ornekte listeleri kullanarak bir ornek yapılacak
Fakat mülakatcı queue kullanarak yapta diyebilir yada baska birsey.
"""


class Stack():
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def showLast(self):
        return self.elements[len(self.elements)-1]

    def size(self):
        return len(self.elements)


myStack = Stack()
print(myStack.isEmpty())
myStack.push(20)
myStack.push(40)
myStack.push(60)
print(myStack.showLast())
print(myStack.size())
myStack.pop()
print(myStack)
print(myStack.pop())

# Stack icersindek elemanları nasıl reverse ederiz diye sorarlarsa
# pop edilen tüm stack elemanlarını bir başka listeye atarak reverse edebiliriz.


