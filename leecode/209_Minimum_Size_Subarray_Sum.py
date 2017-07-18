#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        left = right = 0
        total = 0
        min_size = len(nums) + 1
        while right < len(nums):
            while total < s and right < len(nums):
                total += nums[right]
                right += 1
            if total < s:
                break
            while total >= s:
                total -= nums[left]
                left += 1
            min_size = min(min_size, right - left + 1)

        return 0 if min_size == len(nums) + 1 else min_size
