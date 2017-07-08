#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return None

        nums.sort()

        max1 = nums[-3] * nums[-2] * nums[-1]
        max2 = nums[0] * nums[1] * nums[-1]
        return max(max1, max2)
