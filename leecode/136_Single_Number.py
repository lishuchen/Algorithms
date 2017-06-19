#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return []

        rsl = 0
        for val in nums:
            rsl ^= val

        return rsl
