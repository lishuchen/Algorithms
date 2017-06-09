#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# method 1: rolling array
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not len(matrix):
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0
        max_square = [[0] * cols for _ in range(2)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    max_square[i % 2][j] = min(self.search((i - 1) % 2, j - 1, max_square),
                                               self.search((i - 1) % 2, j, max_square),
                                               self.search(i % 2, j - 1, max_square)) + 1
                    max_area = max(max_area, max_square[i % 2][j])

        return max_area ** 2

    def search(self, i, j, max_square):
        if i < 0 or j < 0:
            return 0
        return max_square[i][j]


# Solution 2: add a extra all-'0' layer
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not len(matrix):
            return 0

        max_area = 0
        prev = [0] * len(matrix[0])
        for row in matrix:
            current = map(int, row)
            for i, val in enumerate(current[1:], 1):
                if current[i] == 1:
                    current[i] = min(prev[i - 1], prev[i], current[i - 1]) + 1
            max_area = max(max_area, max(current) ** 2)
            prev = current

        return max_area

if __name__ == '__main__':
    s = Solution()
    print(s.maximalSquare(["10100","10111","11111","10010"]))