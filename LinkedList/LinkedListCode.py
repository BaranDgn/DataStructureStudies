# Node --> Linked List

# Mülakatta Node in ne oldugunu bilmemizi istiyebilirler.
"""
SINGLY LINKED LIST
    İçinde sadece bir adet Değere referans tutan, diğeri de bir sonraki düğümün ne olacağını tutan
    bir yapıdır.
"""


# SINGLY LINKED LIST
class Node():
    def __init__(self, value):
        self.value = value
        self.nextNode = None


firstNode = Node(10)
secondNode = Node(20)
thirdNode = Node(30)

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode

print(firstNode.value)  # Accessing FirstNode Value
print(firstNode.nextNode.value)  # Accessing second node value over firstNode
print(firstNode.nextNode.nextNode.value)  # Accessing third node value over firstNode


# Doubly LINKED LIST
class DoublyNode():

    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.previousNode = None


x = DoublyNode(5)
y = DoublyNode(10)
z = DoublyNode(15)

x.nextNode = y
y.nextNode = z
y.previousNode = x
z.previousNode = y

print(x.nextNode.nextNode.value) #  Accesing z value over x node
print(z.previousNode.previousNode.value) #  Accesing x value over z node
# be able to access y node's value over both x and z node because this is doubly linked list
print(x.nextNode.value)
print(z.previousNode.value)