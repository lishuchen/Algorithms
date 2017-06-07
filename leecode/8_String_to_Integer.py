#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        str = str.lstrip().rstrip()

        has_sign = 0
        sign = 1
        if str[0] == "-":
            sign = -1
            has_sign = 1
        elif str[0] == "+":
            has_sign = 1
        rsl = 0
        for c in str[has_sign:]:
            if '0' <= c <= '9':
                rsl = rsl * 10 + int(c)
            else:
                break

        if rsl > 2147483647 and sign == 1:
            return 2147483647
        if rsl > 2147483648 and sign == -1:
            return -2147483648

        return sign * rsl