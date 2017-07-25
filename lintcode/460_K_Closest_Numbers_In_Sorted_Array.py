#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @param {int} k a non-negative integer
    # @return {int[]} an integer array
    def kClosestNumbers(self, A, target, k):
        # Write your code here
        if not A or k <= 0:
            return []

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid

        if A[end] - target < target - A[start]:
            start = end

        rsl = [A[start]]

        i = j = 1
        for _ in range(k - 1):
            if start - i < 0 and start + j > len(A) - 1:
                break

            right = left = sys.maxsize
            if start + j < len(A):
                right = abs(A[start + j] - target)
            if start - i > -1:
                left = abs(A[start - i] - target)

            if right >= left:
                rsl.append(A[start - i])
                i += 1
            else:
                rsl.append(A[start + j])
                j += 1

        return rsl
