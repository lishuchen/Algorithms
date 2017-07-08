#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        max_cur = max_contain_end = nums[0]
        for val in nums[1:]:
            max_contain_end = val + max(max_contain_end, 0)
            max_cur = max(max_cur, max_contain_end)

        return max_cur
