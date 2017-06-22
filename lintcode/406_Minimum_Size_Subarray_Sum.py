#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param nums: a list of integers
    # @param s: an integer
    # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        # write your code here
        if not nums:
            return -1

        start = end = 0
        min_size = len(nums) + 1
        total_sum = 0
        while end < len(nums):
            while total_sum < s and end < len(nums):
                total_sum += nums[end]
                end += 1
            while total_sum >= s:
                min_size = min(min_size, end - start)
                total_sum -= nums[start]
                start += 1

        return min_size if min_size != len(nums) + 1 else -1
