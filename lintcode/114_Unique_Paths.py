#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        if m < 0 or n < 0:
            return 0

        pre = [1] * n
        for i in range(1, m):
            cur = [1]
            for j in range(1, n):
                cur.append(pre[j] + cur[j - 1])

            pre = cur

        return pre[-1]
