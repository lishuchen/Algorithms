#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """

    def majorityNumber(self, nums):
        # write your code here
        if not nums:
            return -1

        n = nums[0]
        count = 1
        for num in nums[1:]:
            if num == n:
                count += 1
            else:
                count -= 1
                if count == 0:
                    n = num
                    count = 1

        return n
