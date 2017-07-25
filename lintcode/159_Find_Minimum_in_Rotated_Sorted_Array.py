#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        # write your code here
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]

            mid = start + (end - start) / 2
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid

        return nums[start]
