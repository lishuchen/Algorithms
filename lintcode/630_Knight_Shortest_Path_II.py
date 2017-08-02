#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {boolean[][]} grid a chessboard included 0 and 1
    # @return {int} the shortest path
    def shortestPath2(self, grid):
        # Write your code here
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        dq = collections.deque([(0, 0)])
        grid[0][0] = 2

        step = 0
        while dq:
            step += 1
            size = len(dq)
            for _ in range(size):
                x, y = dq.popleft()
                for i, j in [(1, 2), (-1, 2), (2, 1), (-2, 1)]:
                    new_x, new_y = x + i, y + j
                    if -1 < new_x < rows and -1 < new_y < cols and grid[new_x][new_y] == 0:
                        if new_x == rows - 1 and new_y == cols - 1:
                            return step
                        grid[new_x][new_y] = 2
                        dq.append((new_x, new_y))

        return -1
