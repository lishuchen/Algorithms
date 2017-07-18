#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        dct = dict()
        self.find(root, dct)
        lst = sorted(dct.items(), key=lambda x: x[1], reverse=True)

        max_count = lst[0][1]
        rsl = list()
        for item in lst:
            if item[1] == max_count:
                rsl.append(item[0])
            else:
                break

        return rsl

    def find(self, node, dct):
        if not node:
            return 0

        val = node.val + self.find(node.left, dct) + self.find(node.right, dct)
        if val in dct:
            dct[val] += 1
        else:
            dct[val] = 1

        return val
