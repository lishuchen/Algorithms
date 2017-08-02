#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        if not s:
            return []

        rsl = list()
        self.find(s, 0, [], rsl)

        return rsl

    def find(self, s, start, cur, rsl):
        if start == len(s):
            rsl.append(cur)

        for j in range(start, len(s)):
            part = s[start: j + 1]
            if self.is_pldr(part):
                self.find(s, j + 1, cur + [part], rsl)

    def is_pldr(self, s):
        if len(s) == 1:
            return True

        start, end = 0, len(s) - 1
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False

        return True
