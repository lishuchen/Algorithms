#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param A: A list of integer
    @return: The number of element in the array that
             are smaller that the given integer
    """

    def countOfSmallerNumber(self, A, queries):
        # write your code here
        if not A:
            return [0] * len(queries)

        sort_A = sorted(A)
        l = list()
        for val in queries:
            l.append(self.binary_search(sort_A, val))

        return l

    def binary_search(self, A, val):
        s = 0
        e = len(A) - 1
        while s <= e:
            mid = (s + e) / 2
            if A[mid] >= val:
                if mid == 0:
                    return 0
                else:
                    if A[mid - 1] < val:
                        return mid
                    else:
                        e = mid - 1
            else:
                s = mid + 1

        return len(A)
