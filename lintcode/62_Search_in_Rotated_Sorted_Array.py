#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """

    def search(self, A, target):
        # write your code here
        if not A:
            return -1

        start, end = 0, len(A) - 1
        while start <= end:
            mid = start + ((end - start) >> 1)
            if A[mid] == target:
                return mid
            # left is ordered
            if A[mid] > A[end]:
                if A[start] <= target < A[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # right is ordered
            else:
                if A[mid] < target <= A[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1
