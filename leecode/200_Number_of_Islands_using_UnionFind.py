#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from leecode.DataStruct.UnionFindSet import UnionFind


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        self.rows = len(grid)
        self.cols = len(grid[0])

        uf = UnionFind()
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == "1":
                    index = self.toindex(i, j)
                    uf.add(index, index)

        # 4 directions
        t_x = [0, 0, -1, 1]
        t_y = [-1, 1, 0, 0]

        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == "1":
                    # 4 directions
                    item_a = self.toindex(i, j)
                    for k in range(4):
                        x = i + t_x[k]
                        y = j + t_y[k]
                        if -1 < x < self.rows and -1 < y < self.cols:
                            if grid[x][y] == "1":
                                item_b = self.toindex(x, y)
                                uf.union(item_a, item_b)
                    grid[i] = grid[i][:j] + "0" + grid[i][j + 1:]

        for key in uf.nodes.keys():
            uf.find(key)
        return len(set(uf.nodes.values()))

    def toindex(self, i, j):
        return i * self.cols + j


if __name__ == "__main__":
    s = Solution()
    print(s.numIslands(["11000", "11000", "00100", "00011"]))
    print(s.numIslands(["11110", "11010", "11000", "00000"]))
