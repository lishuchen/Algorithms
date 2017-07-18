#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return []

        self.sum = 0
        self.convert(root)

        return root

    def convert(self, node):
        if not node:
            return

        self.convert(node.right)
        node.val += self.sum
        self.sum = node.val
        self.convert(node.left)
