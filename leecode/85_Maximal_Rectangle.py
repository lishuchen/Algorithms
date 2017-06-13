#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# TODO:

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0
        pre = [[0, 0] for _ in range(cols + 1)]
        for row in matrix:
            cur = [[0, 0]] + list(map(int, row))
            for j, val in enumerate(cur[1:], 1):
                if val == 0:
                    cur[j] = [0, 0]
                else:
                    if cur[j - 1][0] == 0:
                        length = 1
                        width = pre[j][1] + 1
                    elif pre[j][1] == 0:
                        width = 1
                        length = cur[j - 1][0] + 1
                    else:
                        length = min(cur[j - 1][0], pre[j - 1][0]) + 1
                        width = min(pre[j - 1][1], pre[j][1]) + 1
                    cur[j] = [length, width]
                    max_area = max(max_area, length * width)
            pre = cur
            print(cur)

        return max_area


if __name__ == '__main__':
    s = Solution()
    input = ["101101", "111111", "011011", "111010", "011111", "110111"]
    for row in input:
        print(list(map(int, row)))
    s.maximalRectangle(input)
