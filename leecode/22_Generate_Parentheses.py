#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.make("", n, n, [])

    def make(self, cur, n, m, combines):
        if m == 0:
            combines.append(cur)
        if n:
            self.make(cur + '(', n - 1, m, combines)

        if n < m:
            self.make(cur + ")", n, m - 1, combines)

        return combines
