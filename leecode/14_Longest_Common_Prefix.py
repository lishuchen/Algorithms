#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, char in enumerate(strs[0]):
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]

        return strs[0]
