#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumClosest(self, nums, target):
        # Write your code here
        if not nums:
            return -1

        nums.sort()
        start, end = 0, len(nums) - 1
        min_dif = sys.maxsize
        while start < end:
            total = nums[start] + nums[end]
            if total == target:
                return 0
            elif total > target:
                min_dif = min(min_dif, total - target)
                end -= 1
            else:
                min_dif = min(min_dif, target - total)
                start += 1

        return min_dif
