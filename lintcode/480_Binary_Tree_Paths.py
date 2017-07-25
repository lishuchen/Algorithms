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
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        paths = list()
        self.find(root, paths, "")

        return paths

    def find(self, root, paths, cur):
        if not root:
            return

        if cur == "":
            string = str(root.val)
        else:
            string = cur + "->" + str(root.val)

        if root.left is None and root.right is None:
            paths.append(string)

        self.find(root.left, paths, string)
        self.find(root.right, paths, string)
