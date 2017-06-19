#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_bld(root)[1]

    def is_bld(self, root):
        if not root:
            return [0, True]

        left = self.is_bld(root.left)
        right = self.is_bld(root.right)
        if not left[1] or not right[1] or abs(left[0] - right[0]) > 1:
            return [0, False]

        return [1 + max(left[0], right[0]), True]
