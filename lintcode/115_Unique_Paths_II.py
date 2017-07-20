#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        if not obstacleGrid:
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        pre = []
        has_ob = False
        for n in obstacleGrid[0]:
            if has_ob:
                pre.append(0)
            else:
                if n == 1:
                    has_ob = True
                    pre.append(0)
                else:
                    pre.append(1)

        for i in range(1, rows):
            cur = []
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    cur.append(0)
                else:
                    if j == 0:
                        cur.append(pre[0])
                    else:
                        cur.append(pre[j] + cur[j - 1])
            pre = cur

        return pre[-1]
