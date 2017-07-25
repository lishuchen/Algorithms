#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """

    def permuteUnique(self, nums):
        # write your code here
        if nums is None:
            return []

        if nums == []:
            return [[]]

        nums.sort()
        rsl = []
        used = [False] * len(nums)
        self.pmt(nums, rsl, [], used)

        return rsl

    def pmt(self, nums, rsl, cur, used):
        if len(cur) == len(nums):
            rsl.append(cur)
        else:
            for i, num in enumerate(nums):
                if used[i] or (i > 0 and num == nums[i - 1] and not used[i - 1]):
                    continue
                used[i] = True
                self.pmt(nums, rsl, cur + [num], used)
                used[i] = False
