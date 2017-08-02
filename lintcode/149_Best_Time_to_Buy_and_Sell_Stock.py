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

        min_price = prices[0]
        max_profit = 0
        for prc in prices:
            min_price = min(min_price, prc)
            max_profit = max(max_profit, prc - min_price)

        return max_profit
