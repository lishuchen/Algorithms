#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x >= 0 else -1
        x *= flag
        rsl = int(str(x)[::-1])
        return flag * rsl if rsl < 2**31 else 0