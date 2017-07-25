#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param A: An integers list.
    # @return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        if not A:
            return None

        start, end = 0, len(A) - 1
        while start < end:
            mid = start + (end - start) / 2
            if A[mid] > A[mid + 1]:
                end = mid
            else:
                start = mid + 1

        return start
