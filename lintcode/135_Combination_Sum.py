#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates:
            return []

        candidates = list(set(candidates))
        candidates.sort()
        rsl = []
        self.find(candidates, target, [], 0, rsl)

        return rsl

    def find(self, candidates, target, cur, start, rsl):
        if target == 0:
            rsl.append(cur)
            return

        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return

            self.find(candidates, target - candidates[i], cur + [candidates[i]], i, rsl)
