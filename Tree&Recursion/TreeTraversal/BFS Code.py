# BFS CODE

"""
        38
    19      69
12    24  59   95

Asagıdaki Value cıktısına ulasabilmek icin;
Yukarıdaki agacı Queue icersiine sırayla koyuyoruz. Node un kendisini koyuyoruz left i right i dahil.
önce node daki degeri queue ya ekle, sonra leftini ve right ını ekle ve kendisini cıkar.
38 i queue koydum(degerini), sonra 19 ve 69 u Queue koyarken 38 cıkarmak.
19 in degerini yazdım, left ini ve right ini 12 ve 24 u Queue ya koydum. Sırada 69 var,
aynı sekilde kendisini uque ya ekledim ve left ve right olan 59 ve 95 ekledim ve kendisini cıkardım.
en altaki 12, 24, 59, 95 in alt node ları olmadıgı icin kendilerini queu ya ekleyip, cıkarmak.


Queue = [38]
Queue = [19, 69]
Queue = [69, 12, 24]
Queue = [12, 24, 59, 95]

Bir adet Queue yardımıyla BFS code u yazmak.
Algoritma aslında node ları sırasıyla Queue eklemek ve degeri yazdıktan sonra
pop() ederken left ini ve right ini ekleyerek devam etmek.
Queue kullanmamızın olmasının mantıgı ise; ilk girenin ilk çıkmasıdır, bu sayede 19 dan sonra 69 yazdırarak
yatay olarak gezinebilecegim.

Output : Values = [38, 19, 69, 12, 24, 59, 95]

"""


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):

        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            return True

        tempNode = self.root

        while True:

            if newNode.value == tempNode.value:
                return False

            if newNode.value < tempNode.value:
                if tempNode.left is None:
                    tempNode.left = newNode
                    return True
                tempNode = tempNode.left

            else:
                if tempNode.right is None:
                    tempNode.right = newNode
                    return True
                tempNode = tempNode.right

    def contains(self, value):
        tempNode = self.root

        while tempNode:
            if value < tempNode.value:
                tempNode = tempNode.left
            elif value > tempNode.value:
                tempNode = tempNode.right
            else:
                return True
        return False

    def minOfNode(self, currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode

    def maxOfNode(self, currentNode):
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode

    def BFS(self):
        currentNode = self.root
        values = []
        myQueue = []
        myQueue.append(currentNode)

        while len(myQueue) > 0:
            currentNode = myQueue.pop(0)
            values.append(currentNode.value)
            if currentNode.left is not None:
                myQueue.append(currentNode.left)
            if currentNode.right is not None:
                myQueue.append(currentNode.right)
        return values


# liste icindeki verileri agaca ekleme- tek tek ekleme ile ugrasmamak icin

tree = BinarySearchTree()
tree.insert(38)
tree.insert(19)
tree.insert(69)
tree.insert(12)
tree.insert(24)
tree.insert(59)
tree.insert(95)

print(tree.BFS())






















