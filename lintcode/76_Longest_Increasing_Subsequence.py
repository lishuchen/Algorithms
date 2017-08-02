#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0

        size = len(nums)
        dp = [1] * size
        max_len = 0

        for i in range(size):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

            max_len = max(max_len, dp[i])

        return max_len
