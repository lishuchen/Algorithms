#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param: : An integer
    @param: : An integer array
    @return: Maximum profit
    """

    def maxProfit(self, K, prices):
        # write your code here
        if not prices:
            return 0

        days = len(prices)
        if K >= days:
            return self.profit(prices)

        cur = [0] * (K + 1)
        profits = [0] * (K + 1)

        for i in range(1, len(prices)):
            dif = prices[i] - prices[i - 1]
            for j in range(K, 0, -1):
                cur[j] = max(profits[j - 1] + max(dif, 0), cur[j] + dif)
                profits[j] = max(cur[j], profits[j])

        return profits[-1]

    def profit(self, prices):
        sum = 0
        for i in range(1, len(prices)):
            dif = prices[i] - prices[i - 1]
            if dif > 0:
                sum += dif

        return sum
