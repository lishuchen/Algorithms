#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = num
        mask = 0x1
        while a:
            a >>= 1
            mask <<= 1
        return (mask - 1) ^ num