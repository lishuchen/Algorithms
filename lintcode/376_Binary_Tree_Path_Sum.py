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
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        rsl = list()
        self.find(root, target, rsl, [])

        return rsl

    def find(self, root, target, rsl, cur):
        if not root:
            return

        if root.left is None and root.right is None and root.val == target:
            rsl.append(cur + [root.val])
            return

        self.find(root.left, target - root.val, rsl, cur + [root.val])
        self.find(root.right, target - root.val, rsl, cur + [root.val])
