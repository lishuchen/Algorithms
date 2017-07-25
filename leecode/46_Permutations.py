#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        self.result = list()
        self.pmt(nums, [])

        return self.result

    def pmt(self, nums, cur):
        if len(cur) == len(nums):
            self.result.append(cur)
        else:
            for num in nums:
                if num not in cur:
                    self.pmt(nums, cur + [num])
