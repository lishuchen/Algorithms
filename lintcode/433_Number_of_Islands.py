#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count += 1
                    self.mask(grid, i, j)

        return count

    def mask(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == 1:
            grid[i][j] = 0
            offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in offsets:
                self.mask(grid, i + x, j + y)
