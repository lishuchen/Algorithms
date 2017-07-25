#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        start, end = 0, rows * cols - 1
        while start <= end:
            mid = (start + end) / 2
            num = matrix[mid / cols][mid % cols]
            if num == target:
                return True
            elif num > target:
                end = mid - 1
            else:
                start = mid + 1

        return False
