#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum6(self, nums, target):
        # Write your code here
        if not nums:
            return 0

        nums.sort()
        start, end = 0, len(nums) - 1
        count = 0
        while start < end:
            total = nums[start] + nums[end]
            if total == target:
                count += 1
                start += 1
                while nums[start] == nums[start - 1] and start < end:
                    start += 1
                end -= 1
                while nums[end] == nums[end + 1] and start < end:
                    end -= 1
            elif total > target:
                end -= 1
                while nums[end] == nums[end + 1] and start < end:
                    end -= 1
            else:
                start += 1
                while nums[start] == nums[start - 1] and start < end:
                    start += 1

        return count
