# Binary TreeQ Max Path Sum

"""
A path in a binary tree is a sequence of nodes where each pair of adjacent modes in the sequence has an edge connecting them.
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Example1:

        1

    2       3

Input = root= [1,2,3]
Ouput = 6
Explanation = The optional path is 2 -> 1 -> 3 with a path sum of 2 +1 +3 = 6.

Example 2:

        -10
    9       20
         15     7
Input = root= [-10,9,20,null,null,15,7]
Ouput = 42
Explanation = The optional path is 15 -> 20 -> 7 with a path sum of 15 +20 +7 = 42.


"""
import self as self

"""
Soruda herhangi bir route alınacak ağac uzerinde, ve bir branch ten geçilen yani bir yoldan
geçildiğin tekrar kullanılamayacak bu yol.
Bu na göre çizebileceğimiz route lardan toplmaları en büyük olanı bulun diyor.
 
 
         -10
    9       20
         15     7
         
Buna  göre,
    9 --> -10 --> 20 --> 7 : route ini alsam, toplamları : 28 eder. 15 e ugrayamam çünkü uğrarsam 7 yi alamam, aynı yolu tekrar gecemeyeceğim için.
    9 --> -10 --> 20 -->15 : route ini alırsam toplamları 34 eder
    15 --> 20 --> 7 : route ini alırsam, toplamları 42 eder ve görünene göre en büyük değer bu oluyor.
    
SOLUTION 
 Burada DFS algorith kullanmak çok daha mantıklı olacaktır. Çünkü en aşağıdan gidip sub tree lerin değerini öğrenebiliriz.
  
 
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree2:

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

    answer = -float("inf") # - sonsuz tanımı yapıldı

    def maxPathSum(self):
        self.dfs(self.root)
        return self.answer

    def dfs(selfself, node):
        if node is None:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        left = max(left, 0)
        right = max(right, 0)

        self.answer = max(self.answer, node.value + left+right)

        return node.value + max(left, right)


"""
         -10
    9       20
         15     7
"""
tre = BinarySearchTree2()

