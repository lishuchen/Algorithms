#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        start, end = 0, int(math.sqrt(c))
        while start <= end:
            s = start ** 2 + end ** 2
            if s == c:
                return True
            elif s > c:
                end -= 1
            else:
                start += 1

        return False
