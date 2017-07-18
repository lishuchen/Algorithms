#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        tar = dict()
        count = len(t)
        for c in t:
            tar[c] = tar.get(c, 0) + 1

        left = right = 0
        size_s = len(s)
        min_size = size_s + 1
        start = -1
        while right < size_s:
            c = s[right]
            if c in tar:
                tar[c] -= 1
                if tar[c] >= 0:
                    count -= 1
            right += 1
            while count == 0:
                if right - left < min_size:
                    min_size = right - left
                    start = left
                ch = s[left]
                if ch in tar:
                    tar[ch] += 1
                    if tar[ch] > 0:
                        count += 1
                left += 1

        return "" if start == -1 else s[start: start + min_size]
