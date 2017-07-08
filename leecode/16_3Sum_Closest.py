#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return None

        nums.sort()
        diff = sys.maxsize
        for i, val in enumerate(nums[:-2]):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                sum3 = val + nums[start] + nums[end]
                if sum3 == target:
                    return target
                elif sum3 > target:
                    end -= 1
                elif sum3 < target:
                    start += 1
                if abs(sum3 - target) < abs(diff):
                    diff = sum3 - target

        return target + diff
