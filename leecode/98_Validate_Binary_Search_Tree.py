#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1: using int_max
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isvalid(root, -sys.maxint, sys.maxint)

    def isvalid(self, root, min_val, max_val):
        if not root:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False

        return self.isvalid(root.left, min_val, root.val) and self.isvalid(root.right, root.val, max_val)


# Solution 2: using in-order traverse
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if pre is None:
                pre = node.val - 1
            if node.val <= pre:
                return False
            pre = node.val
            root = node.right

        return True
