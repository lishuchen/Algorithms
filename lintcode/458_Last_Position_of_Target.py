#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, A, target):
        # Write your code here
        if not A or target is None:
            return -1

        start, end = 0, lean(A) - 1
        while start < end:
            mid = (start + end) / 2
            if A[mid] <= target:
                start = mid + 1
            else:
                end = mid

        if target == A[start]:
            return start

        if start > 0 and A[start - 1] == target:
            return start - 1

        return -1
