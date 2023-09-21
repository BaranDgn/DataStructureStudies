# Convert BST To Greater TreeQ

"""
Given the "root" of a Binary Search TreeQ(BST), convert it to Greater TreeQ
such that every key of the original BST is changed to the original
key plus the sum of keys greater than the original key in BST.

As a reminder, a binary search three is a tree that satisfies these constraints:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only with keys greater than the node's key.
    Both the left and right subtrees must also be binary trees.

Example1:

                4 -30

     1 -36                 6-21

0-36      2-35       5-26       7 -15

            3-33                       8-8

Input : root = [4,1,6,0,2,5,7, null, null,null,3 null, null, null, 8]
Output : [30,36,21,3 6,35,26,15,null,null,nukk,33,null,null,null,8]

"""
from typing import Optional

import null as null


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def convertBST(selfself, root: Optional[TreeNode]) -> Optional[TreeNode]:

        sumOfValues = 0

        def traverse(node):
            if not node:
                return

            nonlocal sumOfValues
            if node.right is not None:  # node.right is not None -->ile aynısı
                traverse(node.right)

            # node.velue = 8, sumOfvalues= 0
            # temp = 8, node.value = 8, sumofValues = 8
            # node.velue = 7, sumOfvalues= 8
            # temp = 7, node.value = 15, sumofValues = 15
            # node.value = 6, sumOfvalues= 15
            # temp = 6, node.value = 21, sumofValues = 21
            # node.value = 5, sumOfvalues= 15
            # temp = 6, node.value = 21, sumofValues = 21
            temp = node.value
            node.value += sumOfValues
            sumOfValues += temp

            if node.left:
                traverse(node.left)
        traverse(root)
        return root

tree = TreeNode(5)
sol = Solution()


sol.convertBST(5)

"""
        4
    1       6
0     2   5     7
       3           8
"""


