#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if not nums:
            return 0

        i, large = 0, len(nums) - 1
        while i <= large:
            if nums[i] < k:
                i += 1
            else:
                nums[i], nums[large] = nums[large], nums[i]
                large -= 1

        return i
