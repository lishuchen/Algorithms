#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        max_all = max_cur = nums[0]
        for num in nums[1:]:
            max_cur = max(max_cur, 0) + num
            max_all = max(max_cur, max_all)

        return max_all
