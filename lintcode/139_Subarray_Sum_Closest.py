#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """

    def subarraySumClosest(self, nums):
        # write your code here
        if not nums:
            return []

        sum_idx = []
        total = 0
        for i, val in enumerate(nums):
            if val == 0:
                return [i, i]
            total += val
            if total == 0:
                return [0, i]
            sum_idx.append((total, i))

        sum_idx.sort(key=lambda x: x[0])
        # abs
        ans = abs(sum_idx[0][0])
        rsl = [0, sum_idx[0][1]]
        for i in range(1, len(sum_idx)):
            dif = sum_idx[i][0] - sum_idx[i - 1][0]
            if dif < ans:
                ans = dif
                rsl[0] = min(sum_idx[i][1], sum_idx[i - 1][1]) + 1
                rsl[1] = max(sum_idx[i][1], sum_idx[i - 1][1])

        return rsl
