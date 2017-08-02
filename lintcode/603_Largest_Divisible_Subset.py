#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int[]} nums a set of distinct positive integers
    # @return {int[]} the largest subset
    def largestDivisibleSubset(self, nums):
        # Write your code here
        if nums is None or len(nums) < 2:
            return []

        size = len(nums)
        nums.sort()

        dp = [0] * size
        parent = [-1] * size
        max_len = 0
        max_idx = -1
        for i in range(size):
            dp[i] = 1
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = 1 + dp[j]
                        parent[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        ans = list()
        while max_idx != -1:
            ans.append(nums[max_idx])
            max_idx = parent[max_idx]

        return ans
