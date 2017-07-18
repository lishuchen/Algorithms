#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Solution 1: dict
class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    def longestPalindrome(self, s):
        # Write your code here
        if not s:
            return 0

        # key: char value: count
        chars = dict()
        for c in s:
            count = chars.get(c, 0)
            chars[c] = count + 1

        lens = 0
        has_single = False
        for c, count in chars.items():
            if count % 2 == 1:
                has_single = True

            lens += count - count % 2

        return lens + 1 if has_single else lens


# Solution 2: set
class Solution:
    # @param {string} s a string which consists of lowercase or uppercase letters
    # @return {int} the length of the longest palindromes that can be built
    def longestPalindrome(self, s):
        # Write your code here
        if not s:
            return 0

        chars = set()
        for c in s:
            chars.remove(c) if c in chars else chars.add(c)

        return len(s) - len(chars) + 1 if len(chars) > 0 else len(s)
