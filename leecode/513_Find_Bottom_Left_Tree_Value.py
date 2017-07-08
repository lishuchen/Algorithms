#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dq = collections.deque()
        dq.append(root)
        val = root.val
        while dq:
            size = len(dq)
            for i in range(size):
                node = dq.popleft()
                if i == 0:
                    val = node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return val
