#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        o_x = x
        tmp = 0
        while x > 0:
            tmp = tmp*10 + x%10
            x /= 10
        return True if tmp == o_x else False