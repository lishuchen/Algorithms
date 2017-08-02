#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, 0, B, 0, n / 2 + 1)
        else:
            return (self.findKth(A, 0, B, 0, n / 2) + self.findKth(A, 0, B, 0, n / 2 + 1)) / 2.0

    def findKth(self, A, start_A, B, start_B, k):
        if start_A >= len(A):
            return B[start_B + k - 1]
        if start_B >= len(B):
            return A[start_A + k - 1]
        if k == 1:
            return min(A[start_A], B[start_B])

        a_kth = A[start_A + k / 2 - 1] if start_A + k / 2 - 1 < len(A) else sys.maxsize
        b_kth = B[start_B + k / 2 - 1] if start_B + k / 2 - 1 < len(B) else sys.maxsize

        if a_kth < b_kth:
            return self.findKth(A, start_A + k / 2, B, start_B, k - k / 2)
        return self.findKth(A, start_A, B, start_B + k / 2, k - k / 2)
