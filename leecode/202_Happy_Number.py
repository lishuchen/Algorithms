#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dct = dict()
        while True:
            s = 0
            while n:
                n, mod = divmod(n, 10)
                s += mod ** 2
            n = s
            if n == 1:
                return True
            if n in dct:
                return False
            else:
                dct[n] = 0
