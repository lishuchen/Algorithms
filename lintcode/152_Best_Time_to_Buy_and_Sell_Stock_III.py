#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# DP
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0

        days = len(prices)
        k = 2
        local = [[0] * (k + 1) for _ in range(days)]
        profits = [[0] * (k + 1) for _ in range(days)]

        for i, pr in enumerate(prices[1:], 1):
            dif = prices[i] - prices[i - 1]
            for j in range(1, k + 1):
                local[i][j] = max(local[i - 1][j] + dif, profits[i - 1][j - 1] + max(dif, 0))
                profits[i][j] = max(local[i][j], profits[i - 1][j])

        return profits[-1][-1]


# DP II, reduced memory
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0

        days = len(prices)
        k = 2
        local = [0] * (k + 1)
        profits = [0] * (k + 1)

        for i, pr in enumerate(prices[1:], 1):
            dif = prices[i] - prices[i - 1]
            for j in range(k, 0, -1):
                local[j] = max(local[j] + dif, profits[j - 1] + max(dif, 0))
                profits[j] = max(local[j], profits[j])

        return profits[-1]
