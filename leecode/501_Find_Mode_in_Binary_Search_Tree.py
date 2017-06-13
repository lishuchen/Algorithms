#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# in-order traverse
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, modes = [], []
        max_count = count = 0
        pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()

            if not pre:
                pre = node

            if node.val == pre.val:
                count += 1
            if node.val != pre.val:
                count = 1

            if count > max_count:
                max_count = count
                modes = [node.val]
            elif count == max_count and node.val != modes[-1]:
                modes.append(node.val)
            pre = node

            root = node.right

        return modes
