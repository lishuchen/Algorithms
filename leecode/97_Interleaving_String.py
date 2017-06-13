#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False

        flag = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        return self.dp(s1, s2, s3, 0, 0, 0, flag)

    def dp(self, s1, s2, s3, i, j, k, flag):
        if flag[i][j] == 1:
            return False

        if k == len(s3):
            return True

        rsl1 = i < len(s1) and s3[k] == s1[i] and self.dp(s1, s2, s3, i + 1, j, k + 1, flag)
        # essential to have a conditional judgment, to avoid extra computation
        if rsl1:
            return True
        rsl2 = j < len(s2) and s3[k] == s2[j] and self.dp(s1, s2, s3, i, j + 1, k + 1, flag)
        if rsl2:
            return True

        flag[i][j] = 1

        return False
