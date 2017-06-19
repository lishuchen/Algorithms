#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_profit = 0
        start = prices[0]
        for val in prices[1:]:
            start = min(val, start)
            max_profit = max(max_profit, val - start)

        return max_profit
