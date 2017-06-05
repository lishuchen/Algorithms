#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        count = 0
        while z:
            count += 1
            # convert the right most "1" to "0"
            z &= z - 1
        return count