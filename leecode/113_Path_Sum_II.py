#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        self.rsl = list()
        self.findall(root, sum, [])

        return self.rsl

    def findall(self, node, sum, path):
        if not node:
            return

        sum -= node.val
        if sum == 0 and node.left is None and node.right is None:
            path.append(node.val)
            self.rsl.append(path)
            return

        self.findall(node.left, sum, path + [node.val])
        self.findall(node.right, sum, path + [node.val])
