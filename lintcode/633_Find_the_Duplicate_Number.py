#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int[]} nums an array containing n + 1 integers which is between 1 and n
    # @return {int} the duplicate one
    def findDuplicate(self, nums):
        # Write your code here
        if not nums:
            return -1

        for i, n in enumerate(nums, 1):
            if nums[abs(n)] < 0:
                return abs(n)
            else:
                nums[abs(n)] *= -1
