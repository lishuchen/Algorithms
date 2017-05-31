#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# !/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        return sum([self.remove(i, j, grid) for i in range(len(grid)) for j in range(len(grid))])

    def remove(self, i, j, grid):
        # 4 directions
        if -1 < i < len(grid) and -1 < j < len(grid[i]) and grid[i][j] == "1":
            grid[i] = grid[i][:j] + "0" + grid[i][j + 1:]
            # 4 directions
            t_x = [0, 0, -1, 1]
            t_y = [-1, 1, 0, 0]
            for k in range(4):
                x = i + t_x[k]
                y = j + t_y[k]
                self.remove(x, y, grid)
            return 1
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    print(s.numIslands(["11000", "11000", "00100", "00011"]))
    print(s.numIslands(["11110", "11010", "11000", "00000"]))
