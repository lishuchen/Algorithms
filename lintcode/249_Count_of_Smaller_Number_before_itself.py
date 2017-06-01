#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param A: A list of integer
    @return: Count the number of element before this element 'ai' is
             smaller than it and return count number list
    """

    def countOfSmallerNumberII(self, A):
        # write your code here
        if not A:
            return []

        root = STree(0, max(A))
        rsl = list()
        for val in A:
            rsl.append(root.count_smaller(0, val - 1))
            root.update(val, 1)

        return rsl


class STree:
    def __init__(self, start, end):
        self.start, self.end, self.count = start, end, 0
        self.left = self.right = None
        if start != end:
            mid = (start + end) / 2
            self.left = STree(start, mid)
            self.right = STree(mid + 1, end)

    def count_smaller(self, start, end):
        if start == self.start and self.end == end:
            return self.count
        if self.start == self.end:
            return 0
        mid = (self.start + self.end) / 2
        if end <= mid:
            return self.left.count_smaller(start, end)
        if start > mid:
            return self.right.count_smaller(start, end)

        return self.left.count_smaller(start, mid) + self.right.count_smaller(mid + 1, end)

    def update(self, index, count):
        if self.start == index == self.end:
            self.count += count

        if self.start == self.end:
            return 0

        mid = (self.start + self.end) / 2
        if index <= mid:
            self.left.update(index, count)
        if index > mid:
            self.right.update(index, count)
        self.count = self.left.count + self.right.count
