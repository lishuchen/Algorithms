#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive(self, root):
        # Write your code here
        self.max_l = 0
        self.longest(root)

        return self.max_l

    def longest(self, root):
        if root is None:
            return [0, 0]

        left_v, left_l = self.longest(root.left)
        right_v, right_l = self.longest(root.right)

        max_l = 0
        if root.val + 1 == left_v:
            max_l = left_l
        if root.val + 1 == right_v:
            max_l = max(max_l, right_l)

        self.max_l = max(self.max_l, max_l + 1)

        return [root.val, max_l + 1]
