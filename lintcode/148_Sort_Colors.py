#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        # write your code here
        if not nums:
            return []

        red = 0
        blue = len(nums) - 1
        i = 0
        while i <= blue:
            if nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
            elif nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
                i += 1
            else:
                i += 1
