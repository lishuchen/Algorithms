#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        return self.find(root)[0]

    def find(self, root):
        if root is None:
            return [True, 0]

        left = self.find(root.left)
        right = self.find(root.right)
        if not left[0] or not right[0] or abs(left[1] - right[1]) > 1:
            return [False, 0]

        return [True, max(left[1], right[1]) + 1]
