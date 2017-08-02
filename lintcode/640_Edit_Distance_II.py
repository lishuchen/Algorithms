#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {string} s a string
    # @param {string} t a string
    # @return {boolean} true if they are both one edit distance apart or false
    def isOneEditDistance(self, s, t):
        # Write your code here
        if s is None or t is None:
            return None

        if abs(len(s) - len(t)) > 1 or s == t:
            return False

        for idx in range(min(len(s), len(t))):
            if s[idx] != t[idx]:
                if s[idx:] == t[idx + 1:] or s[idx + 1:] == t[idx:] or s[idx + 1:] == t[idx + 1:]:
                    return True
                return False

        return True
