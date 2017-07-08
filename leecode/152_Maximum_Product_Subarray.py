#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        max_cur = max_w_end = min_w_end = nums[0]
        for val in nums[1:]:
            if val < 0:
                max_w_end, min_w_end = min_w_end, max_w_end

            max_w_end = max(max_w_end * val, val)
            min_w_end = min(min_w_end * val, val)

            max_cur = max(max_cur, max_w_end)

        return max_cur
