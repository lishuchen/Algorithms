#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """

    def minPathSum(self, grid):
        # write your code here

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        pre = []
        sum = 0
        for val in grid[0]:
            sum += val
            pre.append(sum)

        for row in grid[1:]:
            cur = [pre[0] + row[0]]
            for j in range(1, len(row)):
                cur.append(min(pre[j], cur[j - 1]) + row[j])

            pre = cur

        return pre[-1]
