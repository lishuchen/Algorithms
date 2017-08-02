#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxTwoSubArrays(self, nums):
        # write your code here
        if not nums:
            return None

        left = [0] * len(nums)
        cur_max = total_max = - sys.maxsize - 1
        for i in range(0, len(nums)):
            cur_max = max(cur_max, 0) + nums[i]
            left[i] = total_max = max(cur_max, total_max)

        right = [0] * len(nums)
        cur_max = total_max = - sys.maxsize - 1
        for i in range(len(nums) - 1, -1, -1):
            cur_max = max(cur_max, 0) + nums[i]
            right[i] = total_max = max(cur_max, total_max)

        ans = - sys.maxsize - 1
        for i in range(0, len(nums) - 1):
            ans = max(ans, left[i] + right[i + 1])

        return ans
