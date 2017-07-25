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
    # @return {TreeNode} the root of the minimun subtree
    def findSubtree(self, root):
        # Write your code here
        if not root:
            return None

        self.subnode = None
        self.min = sys.maxsize
        self.minimun(root)

        return self.subnode

    def minimun(self, root):
        if root is None:
            return 0

        total = root.val + self.minimun(root.left) + self.minimun(root.right)
        if self.subnode is None or total < self.min:
            self.min = total
            self.subnode = root

        return total
