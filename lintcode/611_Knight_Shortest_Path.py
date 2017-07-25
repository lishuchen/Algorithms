#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {boolean[][]} grid a chessboard included 0 (False) and 1 (True)
    # @param {Point} source a point
    # @param {Point} destination a point
    # @return {int} the shortest path
    def shortestPath(self, grid, source, destination):
        # Write your code here
        if not grid or grid[source.x][source.y] == 1 or grid[destination.x][destination.y] == 1:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        dq = collections.deque([(source.x, source.y)])
        grid[source.x][source.y] = 2
        step = 0
        while dq:
            size = len(dq)
            step += 1
            for _ in xrange(size):
                x, y = dq.popleft()
                for i, j in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                    if -1 < x + i < rows and -1 < y + j < cols and grid[x + i][y + j] == 0:
                        if x + i == destination.x and y + j == destination.y:
                            return step
                        grid[x + i][y + j] = 2
                        dq.append((x + i, y + j))

        return -1
