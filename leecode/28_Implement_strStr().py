#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle or not needle:
            return 0
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            count = 0
            for j in range(len(needle)):
                if haystack[i + j] == needle[j]:
                    count += 1
                else:
                    break
            if count == len(needle):
                return i

        return -1
