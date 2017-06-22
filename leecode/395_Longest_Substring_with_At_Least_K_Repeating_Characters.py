#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Idea: split by the unqualified char
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for char in set(s):
            if s.count(char) < k:
                return max(self.longestSubstring(string, k) for string in s.split(char))

        return len(s)
