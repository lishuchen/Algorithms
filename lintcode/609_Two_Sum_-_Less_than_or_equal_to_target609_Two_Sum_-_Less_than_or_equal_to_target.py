#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum5(self, nums, target):
        # Write your code here
        if not nums:
            return 0

        nums.sort(reverse=True)
        start, end = 0, len(nums) - 1
        count = 0

        while start < end:
            total = nums[start] + nums[end]
            if total > target:
                start += 1
            else:
                count += end - start
                end -= 1

        return count
