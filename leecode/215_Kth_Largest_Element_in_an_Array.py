#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# method one: using heap
# complexity O(n + k*log(n))
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 0 or k > len(nums):
            return
        h = []
        for val in nums:
            heapq.heappush(h, -val)
        for _ in range(k):
            val = -heapq.heappop(h)

        return val

# TODO: method two: using quickselect
# complexity O(n)