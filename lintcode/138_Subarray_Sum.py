#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        if not nums:
            return []

        sums = dict()
        total = 0
        for i, n in enumerate(nums):
            total += n
            if total == 0:
                return [0, i]
            if total in sums:
                return [sums[total] + 1, i]
            sums[total] = i
