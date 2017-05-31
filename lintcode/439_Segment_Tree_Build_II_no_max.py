#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""


class Solution:
    # @oaram A: a list of integer
    # @return: The root of Segment Tree
    def build(self, A):
        # write your code here
        return self.build_recursive(A, 0)

    def build_recursive(self, B, start_index):
        if B:
            start = 0
            end = len(B) - 1
            node = SegmentTreeNode(start_index + start, start_index + end, B[start])
            if start != end:
                mid = (start + end) / 2
                node.left = self.build_recursive(B[start:mid + 1], start + start_index)
                node.right = self.build_recursive(B[mid + 1:end + 1], start_index + mid + 1)
            if node.left and node.left.max > node.max:
                node.max = node.left.max
            if node.right and node.right.max > node.max:
                node.max = node.right.max
            return node
        return None
