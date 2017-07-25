#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """

    def minSubArray(self, nums):
        # write your code here
        if not nums:
            return 0

        min_all = min_end = nums[0]
        for num in nums[1:]:
            min_end = min(min_end, 0) + num
            min_all = min(min_all, min_end)

        return min_all
