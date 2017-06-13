#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: recursive
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        rsl = []
        rsl += self.inorderTraversal(root.left)
        rsl.append(root.val)
        rsl += self.inorderTraversal(root.right)

        return rsl


# Solution 2: iterate
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, rsl = [], []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            pop_node = stack.pop()
            rsl.append(pop_node.val)
            root = pop_node.right

        return rsl
