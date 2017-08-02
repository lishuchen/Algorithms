#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# set
class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        vals = set()
        for n in nums:
            if n not in vals:
                nums[len(vals)] = n
                vals.add(n)

        return len(vals)


# sort
class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        if not nums:
            return 0

        nums.sort()
        idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[idx] = nums[i]
                idx += 1

        return idx
