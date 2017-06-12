#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        total = 0
        if count:
            for i in range(len(bin(max(nums))[2:])):
                total_ones = sum(list(map(lambda x, j=i: (x >> j) & 0x1, nums)))
                total += (count - total_ones) * total_ones

        return total
