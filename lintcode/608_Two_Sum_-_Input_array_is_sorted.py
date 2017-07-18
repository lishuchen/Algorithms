#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} = nums[index1] + nums[index2]
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):
        # Write your code here
        if not nums:
            return []

        start, end = 0, len(nums) - 1
        while start < end:
            s = nums[start] + nums[end]
            if s == target:
                return [start + 1, end + 1]
            elif s > target:
                end -= 1
            else:
                start += 1
        return []
