#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the root of the maximum average of subtree
    def findSubtree2(self, root):
        # Write your code here
        self.max_root = self.max_avg = None
        self.find(root)

        return self.max_root

    def find(self, node):
        if not node:
            return [0, 0]

        l_sum, l_size = self.find(node.left)
        r_sum, r_size = self.find(node.right)

        sum = node.val + l_sum + r_sum
        size = 1 + l_size + r_size
        avg = sum / float(size)
        if self.max_root is None or avg > self.max_avg:
            self.max_root = node
            self.max_avg = avg

        return [sum, size]
