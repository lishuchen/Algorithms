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

        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if 1 in obstacleGrid[0]:
            idx = obstacleGrid[0].index(1)
            pre = [1] * idx + [0] * (cols - idx)
        else:
            pre = [1] * cols

        for i in range(1, rows):
            cur = [pre[0]] if obstacleGrid[i][0] == 0 else [0]
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    cur.append(0)
                else:
                    cur.append(pre[j] + cur[j - 1])

            pre = cur

        return pre[-1]
