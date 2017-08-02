#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs:
            return ""

        n = len(strs)
        m = min((len(s) for s in strs))

        pref = ""
        for j in range(m):
            ch = strs[0][j]
            count = 0
            for i in range(1, n):
                if strs[i][j] == ch:
                    count += 1
                else:
                    break

            if count == n - 1:
                pref += ch
            else:
                break

        return pref
