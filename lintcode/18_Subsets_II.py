#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, S):
        # write your code here
        if S is None:
            return []
        if S == []:
            return [[]]

        S.sort()
        rsl = []
        self.subset(S, rsl, [], 0)

        return rsl

    def subset(self, nums, rsl, cur, start):
        rsl.append(cur)
        for i, num in enumerate(nums[start:]):
            if i > 0 and num == nums[start + i - 1]:
                continue
            self.subset(nums, rsl, cur + [num], start + i + 1)
