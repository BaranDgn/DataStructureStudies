# DFS Code

"""
        38
    19      69
12    24  59   95

DFS için 3 farklı yoluda yapalım.

1. preOrder
    Önce roottan baslayarak, soldan devam eder sırasıyla 19 sonra 12 ve artık sol taraftaki en dipteki node dan sora bir sey yoksa
    bunun hemen bir sag tarafına bakarız birsey var mı diye, varsa ekleriz.

    sol tarafı gzdikten sonra daha sonra sag tarafa donuyoruz. sırasıyla 69 - 69- 95.

    Values = [38, 19, 12, 24, 69,59,95]
2. PostOrder


3. InOrder

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

    def DFSPreOrder(self):
        values = []

        def traverse(currentNode):
            values.append(currentNode.value)
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
        traverse(self.root)
        return values

    def DFSPostOrder(self):
        values = []

        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
            values.append(currentNode.value)
        traverse(self.root)
        return values

    def DFSInOrder(self):
        values = []

        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            values.append(currentNode.value)
            if currentNode.right is not None:
                traverse(currentNode.right)

        traverse(self.root)
        return values



tree = BinarySearchTree()
tree.insert(38)
tree.insert(19)
tree.insert(69)
tree.insert(12)
tree.insert(24)
tree.insert(59)
tree.insert(95)

print(tree.DFSPreOrder())
print(tree.DFSPostOrder())
print(tree.DFSInOrder())