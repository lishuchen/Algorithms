#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int[]} nums a mountain sequence which increase firstly and then decrease
    # @return {int} then mountain top
    def mountainSequence(self, nums):
        # Write your code here
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) / 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1

        return nums[start]
