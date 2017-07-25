#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # write your code here
        if x < 0:
            return -1

        start = 0
        end = x

        while start + 1 < end:
            mid = (start + end) >> 1
            num = mid ** 2
            if mid ** 2 == x:
                return mid
            elif num > x:
                end = mid
            else:
                start = mid

        return end if end ** 2 <= x else start
