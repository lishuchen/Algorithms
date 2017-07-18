#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: traverse
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False

        return self.check(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def check(self, src, tar):
        if src == None or tar == None:
            return True if src == tar else False

        return src.val == tar.val and self.check(src.left, tar.left) and self.check(src.right, tar.right)
