#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import heapq


class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """

    def medianII(self, nums):
        # write your code here
        if not nums:
            return []

        # left: max_heap
        # right: min_heap
        left, right = [], []
        heapq.heappush(left, -nums[0])
        medians = [nums[0]]

        for num in nums[1:]:
            if len(left) <= len(right):
                heapq.heappush(left, -heapq.heappushpop(right, num))
            else:
                heapq.heappush(right, -heapq.heappushpop(left, -num))

            medians.append(-left[0])

        return medians
