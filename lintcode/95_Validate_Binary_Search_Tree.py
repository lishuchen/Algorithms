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
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here
        if not root:
            return True

        stack = list()
        pre = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pre and root.val <= pre:
                return False

            pre = root.val
            root = root.right

        return True
