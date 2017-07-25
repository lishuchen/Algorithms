#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer
    def zombie(self, grid):
        # Write your code here
        if not grid:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        dq = collections.deque()
        count = rows * cols
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dq.append((i, j))
                    count -= 1
                elif grid[i][j] == 2:
                    count -= 1

        days = 0
        while dq:
            days += 1
            size = len(dq)
            for _ in range(size):
                x, y = dq.popleft()
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if -1 < x + i < rows and -1 < y + j < cols and grid[x + i][y + j] == 0:
                        grid[x + i][y + j] = 1
                        dq.append((x + i, y + j))
                        count -= 1

        return days - 1 if count == 0 else -1
