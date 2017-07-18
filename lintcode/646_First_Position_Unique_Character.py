#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {string} s a string
    # @return {int} it's index
    def firstUniqChar(self, s):
        # Write your code here
        dct = dict()

        for index, c in enumerate(s):
            dct.setdefault(c, []).append(index)

        fst_idx = len(s)
        for c, lst in dct.items():
            if len(lst) == 1:
                fst_idx = min(fst_idx, lst[0])

        return -1 if fst_idx == len(s) else fst_idx
