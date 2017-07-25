#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# recursive
# !/usr/bin/env python
# -*- coding: UTF-8 -*-

# recursive
class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """

    def subsets(self, S):
        # write your code here
        if S is None:
            return []

        self.rsl = []
        S.sort()
        self.sub(S, 0, [])

        return self.rsl

    def sub(self, S, start, cur):
        self.rsl.append(cur)

        for i, val in enumerate(S[start:], 1):
            self.sub(S, start + i, cur + [val])
