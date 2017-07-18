#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import heapq


class Solution:
    # @param {int[][]} arrays a list of array
    # @param {int} k an integer
    # @return {int} an integer, K-th largest element in N arrays
    def KthInArrays(self, arrays, k):
        # Write your code here
        if not arrays and k <= 0:
            return -1

        hp = []
        for arr in arrays:
            for val in arr:
                heapq.heappush(hp, -val)

        for _ in range(k - 1):
            if hp:
                heapq.heappop(hp)

        return -heapq.heappop(hp) if hp else -1
