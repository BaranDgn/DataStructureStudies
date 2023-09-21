# Insert Method


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

        tempNode = self.root  # root u degistirmemek icin olusturuldu.
        # root dolu ise
        while True:
            if newNode.value == tempNode.value:
                return False
            if newNode.value < tempNode.value:
                if tempNode.left is None:
                    tempNode.left = newNode
                    return True
                tempNode = tempNode.left  # root dısında baska node lar varsa eklemeden once ki son node a kadar node u atıyoruz. kontrol icin
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
        return True

    # En kucugu bulmak icin sadece agacın soluna bakmak yeterlidir.
    def minOfNode(self, currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode

    def maxOfNode(self, currentNode):
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode



"""
        10
      8     80
    1     18   96
            25
"""
myTree = BinarySearchTree()
print(myTree.insert(10))
print(myTree.insert(8))
print(myTree.insert(80))
print(myTree.insert(96))
print(myTree.insert(18))
print(myTree.insert(1))
print(myTree.insert(25))

print(myTree.contains(80))
print("--------")
print("min value of TreeQ: ", myTree.minOfNode(myTree.root).value)
print("max value of TreeQ: ", myTree.maxOfNode(myTree.root).value)

print("----------")
print(myTree.root.value) # 10
print(myTree.root.right.value) # 80
print(myTree.root.left.value) # 8
print("-------------")
print(myTree.root.right.right.value) # 96
print(myTree.root.right.right) # <__main__.Node object at 0x000001273F06F8B0>
print(myTree.root.right.left.value) #  18
print(myTree.root.left.left.value) #  1
#print(myTree.root.left.right.value) # None

"""
        10
      8     80
    1     18   96
            25
"""


