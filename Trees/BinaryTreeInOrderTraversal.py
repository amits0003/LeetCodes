"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""


class TreeNode1:
    right = None

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal1(self, root):
        result = []
        self._inorder_traversal(root, result)
        return result

    def _inorder_traversal(self, node, result):
        if not node:
            return
        self._inorder_traversal(node.left, result)
        result.append(node.val)
        self._inorder_traversal(node.right, result)


solution = Solution()
print("\n Hello \n")

newBinaryTree1 = TreeNode1(1)
hot1 = TreeNode1(2)
cold1 = TreeNode1(3)
newBinaryTree1.left = hot1
newBinaryTree1.right = cold1
solution.inorderTraversal1(newBinaryTree1)
