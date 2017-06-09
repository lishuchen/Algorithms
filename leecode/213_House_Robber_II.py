#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        return max(self.rob_money(nums[:-1]), self.rob_money(nums[1:]))

    def rob_money(self, nums):
        profit = [0, nums[0]]
        for i in range(2, len(nums) + 1):
            profit[i % 2] = max(profit[(i - 1) % 2], profit[i % 2] + nums[i - 1])
        return profit[len(nums) % 2]