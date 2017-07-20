#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        rsl = [1, 1]
        for i in range(2, n + 1):
            rsl.append(rsl[i - 1] + rsl[i - 2])

        return rsl[-1]
