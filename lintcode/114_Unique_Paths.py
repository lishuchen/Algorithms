#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """

    def uniquePaths(self, m, n):
        # write your code here
        pre = [1] * n
        for i in range(1, m):
            cur = []
            for j in range(n):
                if j == 0:
                    cur.append(pre[0])
                else:
                    cur.append(pre[j] + cur[j - 1])
            pre = cur

        return pre[-1]
