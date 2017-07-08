#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return None

        n = len(matrix)
        flags = [[0] * n for _ in range(n)]

        hp = [(matrix[0][0], 0, 0)]
        flags[0][0] == True

        for _ in range(k - 1):
            val, i, j = heapq.heappop(hp)
            new_i = i + 1
            if i < n - 1 and flags[new_i][j] == 0:
                heapq.heappush(hp, (matrix[new_i][j], new_i, j))
                flags[new_i][j] = 1
            new_j = j + 1
            if j < n - 1 and flags[i][new_j] == 0:
                heapq.heappush(hp, (matrix[i][new_j], i, new_j))
                flags[i][new_j] = 1

        return heapq.heappop(hp)[0]
