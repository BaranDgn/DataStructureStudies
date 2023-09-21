# Invert Binary TreeQ -- Google

"""
Given the root of binary tree, invert the tree and return its root.

Example 1:
        4                         4
    2       7         -->    7        2
1     3   6    9          9    6   3    1

Input : root = [4,2,7,1,3,6,9]
Output = [4,7,2,9,6,3,1]


Example 2:
        2                         2
    1       3         -->    3        1


Input : root = [2,1,3]
Output = [2,3,1]

"""
from typing import Optional


class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Exit condition
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        # recursion
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



solution = Solution()
print(solution.invertTree(TreeNode))
