#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = [1, 2]
        for i in range(2, n):
            counts.append(counts[i - 1] + counts[i - 2])

        return counts[n - 1]
