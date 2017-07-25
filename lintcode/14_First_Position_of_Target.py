#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid + 1

        return start if target == nums[start] else -1
