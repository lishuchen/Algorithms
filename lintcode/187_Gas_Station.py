#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Greedy
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        if not gas or not cost:
            return -1

        if len(gas) == 1:
            if gas[0] < cost[0]:
                return -1
            else:
                return 0

        cur_sum = total = start = 0
        for i in range(len(gas)):
            dif = gas[i] - cost[i]
            total += dif
            cur_sum += dif
            if cur_sum < 0:
                start = i + 1
                cur_sum = 0

        return -1 if total < 0 else start
