#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return
        d = dict()
        for index, val in enumerate(nums):
            tmp = target - val
            if tmp in d:
                return [d[tmp], index]
            else:
                d[val] = index