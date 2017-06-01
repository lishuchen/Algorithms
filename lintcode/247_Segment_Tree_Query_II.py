#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""


class Solution:
    # @param root, start, end: The root of segment tree and
    #                          an segment / interval
    # @return: The count number in the interval [start, end]
    def query(self, root, start, end):
        # write your code here
        if not root or start > end:
            return 0

        if root.start >= start and root.end <= end:
            return root.count

        mid = (root.start + root.end) / 2
        if end <= mid:
            return self.query(root.left, start, end)
        if start > mid:
            return self.query(root.right, start, end)

        return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)
