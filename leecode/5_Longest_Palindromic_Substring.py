#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Solution 1: extend
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0

        max_len = 1
        start_point = 0
        for i in range(len(s) - 1):
            s1, lens1 = self.palind(s, i, i)
            if lens1 > max_len:
                max_len = lens1
                start_point = s1
            s2, lens2 = self.palind(s, i, i + 1)
            if lens2 > max_len:
                max_len = lens2
                start_point = s2

        return s[start_point: start_point + max_len]

    def palind(self, s, left, right):
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        start = left + 1
        lens = right - left - 1

        return start, lens


# Solution 2: expand the size by 1 or 2
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0

        max_len = 1
        start_point = 0
        for i in range(len(s)):
            if self.isPalind(s, i - max_len - 1, i):
                start_point = i - max_len - 1
                max_len += 2
            if self.isPalind(s, i - max_len, i):
                start_point = i - max_len
                max_len += 1
            print(start_point, max_len)

        return s[start_point: start_point + max_len]

    def isPalind(self, s, left, right):
        if left < 0:
            return False

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
