#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        rsl = []
        dq = collections.deque()
        dq.append(root)
        flag = 1
        while dq:
            level = []
            size = len(dq)
            for _ in range(size):
                if flag == 0:
                    node = dq.popleft()
                    if node.right:
                        dq.append(node.right)
                    if node.left:
                        dq.append(node.left)
                else:
                    node = dq.pop()
                    if node.left:
                        dq.appendleft(node.left)
                    if node.right:
                        dq.appendleft(node.right)
                level.append(node.val)

            flag = 0 if flag else 1
            rsl.append(level)

        return rsl
