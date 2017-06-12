#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None

        val = 0
        one_left = one_right = two_left = two_right = None
        if t1:
            val += t1.val
            one_left = t1.left
            one_right = t1.right
        if t2:
            val += t2.val
            two_left = t2.left
            two_right = t2.right

        node = TreeNode(val)
        node.left = self.mergeTrees(one_left, two_left)
        node.right = self.mergeTrees(one_right, two_right)
        return node
