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
    @param A: a list of integer
    @return: a tree node
    """

    def sortedArrayToBST(self, A):
        # write your code here
        if not A:
            return

        mid = len(A) / 2
        root = TreeNode(A[mid])
        root.left = self.sortedArrayToBST(A[:mid])
        root.right = self.sortedArrayToBST(A[mid + 1:])

        return root
