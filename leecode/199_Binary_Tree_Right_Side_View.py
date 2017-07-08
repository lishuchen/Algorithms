#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rsl = list()
        self.view(root, 0, rsl)

        return rsl

    def view(self, node, level, rsl):
        if not node:
            return

        if level == len(rsl):
            rsl.append(node.val)

        self.view(node.right, level + 1, rsl)
        self.view(node.left, level + 1, rsl)
