#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            dif = prices[i] - prices[i - 1]
            if dif > 0:
                profit += dif

        return profit
