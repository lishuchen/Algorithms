#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        rsl = [0]
        for n in range(1, num + 1):
            rsl.append(rsl[n >> 1] + (n % 2))

        return rsl
