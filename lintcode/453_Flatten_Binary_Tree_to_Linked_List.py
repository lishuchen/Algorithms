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
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        cur = TreeNode(0)

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                cur.right = node
                cur.right.left = None
                cur = cur.right
