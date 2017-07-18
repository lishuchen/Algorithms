#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        times = ""
        lst = [[1, ""]]
        for c in s:
            if c.isdigit():
                times += c
            elif c == "[":
                lst.append([int(times), ""])
                times = ""
            elif c == "]":
                t, string = lst.pop()
                lst[-1][1] += string * t
            else:
                lst[-1][1] += c

        return lst[0][1]
