#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]

        rsl = list()
        self.pmt(nums, rsl, [])

        return rsl

    def pmt(self, nums, result, cur):
        if len(cur) == len(nums):
            result.append(cur)
        else:
            for num in nums:
                if num not in cur:
                    self.pmt(nums, result, cur + [num])


# optimized -- remove the searching for the existence
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]

        rsl = list()
        used = [False] * len(nums)
        self.pmt(nums, rsl, [], used)

        return rsl

    def pmt(self, nums, result, cur, used):
        if len(cur) == len(nums):
            result.append(cur)
        else:
            for i, num in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    self.pmt(nums, result, cur + [num], used)
                    used[i] = False
