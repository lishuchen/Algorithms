#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        return sum([nums[2*i] for i in range(len(nums)/2)])