#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None

        x = 0
        for val in nums:
            x ^= val

        rsl = [0, 0]
        mask = x & ~(x - 1)
        for val in nums:
            if val & mask:
                rsl[0] ^= val
            else:
                rsl[1] ^= val

        return rsl
