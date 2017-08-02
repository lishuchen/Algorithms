#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        if not grid:
            return -1

        rows = len(grid)
        cols = len(grid[0])

        cnt_dis = [[[0, 0] for __ in range(cols)] for _ in range(rows)]

        ones = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones += 1

                    self.compute(i, j, grid, cnt_dis)

        min_dis = sys.maxsize
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    if cnt_dis[i][j][0] == ones:
                        min_dis = min(min_dis, cnt_dis[i][j][1])

        return min_dis if min_dis != sys.maxsize else -1

    def compute(self, i, j, grid, cnt_dis):
        visit = [[False] * len(grid[0]) for _ in range(len(grid))]
        dq = collections.deque([(i, j)])
        step = 0
        while dq:
            step += 1
            size = len(dq)
            for _ in range(size):
                x, y = dq.popleft()
                for p, q in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_x = x + p
                    new_y = y + q
                    if -1 < new_x < len(grid) and -1 < new_y < len(grid[0]) and not visit[new_x][new_y]:
                        visit[new_x][new_y] = True
                        if grid[new_x][new_y] == 0:
                            cnt_dis[new_x][new_y][0] += 1
                            cnt_dis[new_x][new_y][1] += step
                            dq.append((new_x, new_y))
