#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return -1

        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0

        for i in range(n + 1):
            j = 0
            while j * j <= i:
                dp[i] = min(dp[i], 1 + dp[i - j * j])
                j += 1

        return dp[n]
