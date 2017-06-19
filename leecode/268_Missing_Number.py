#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Solution 1: sum
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_all = sum(nums)
        return len(nums) * (len(nums) + 1) / 2 - sum_all


# Solution 2: XOR
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rsl = len(nums)
        for i, val in enumerate(nums):
            rsl ^= i ^ val

        return rsl
