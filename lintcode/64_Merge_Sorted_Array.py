#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """

    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        if not A and not B:
            return None

        idx = m + n - 1
        i, j = m - 1, n - 1
        while i > -1 and j > -1:
            if A[i] < B[j]:
                A[idx] = B[j]
                j -= 1
            else:
                A[idx] = A[i]
                i -= 1
            idx -= 1

        if i == -1:
            while j > -1:
                A[idx] = B[j]
                idx -= 1
                j -= 1
