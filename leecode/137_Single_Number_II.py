#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1 = x2 = 0
        for val in nums:
            x2 ^= x1 & val
            x1 ^= val
            # omit the rest when sqrt(k) is an integer
            mask = ~(x2 & x1)
            x2 &= mask
            x1 &= mask

        return x1

# General Solution for problem:
# Find the number in an array of integers where this number appears p times and every other element appears k times .
# Requirement p % k != 0 and p >= 1
# Idea - Using counter for each bit, the number of the counters is the smallest number m satisfying m >= log(k)
# 32 m-bits counters = m 32-bits counters
# traverse set the value of each counter to 0 when reaching k
# return the value of the counters corresponding to the "1"-bit int p % k
#   E.g., 1. p = 1, k = 2 p%k = 0b01 return x1
#         2. p = 3, k = 4 p%k = 0b11 return x1 or x2
#         3. p = 5, k = 3 p%k = 0b10 return x2
