#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, candidates, target):
        # write your code here
        if not candidates:
            return []

        candidates.sort()
        rsl = []
        self.find(candidates, target, 0, [], rsl)

        return rsl

    def find(self, nums, target, start, cur, rsl):
        if target == 0:
            rsl.append(cur)

        for i in range(start, len(nums)):
            if target < nums[i]:
                return
            if i > start and nums[i] == nums[i - 1]:
                continue
            self.find(nums, target - nums[i], i + 1, cur + [nums[i]], rsl)
