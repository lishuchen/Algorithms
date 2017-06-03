#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        # max heap
        self.small = []
        # min heap
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        n_small = len(self.small)
        n_large = len(self.large)
        if n_small >= n_large:
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        else:
            return float(self.large[0])