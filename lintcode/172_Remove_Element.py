#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """

    def removeElement(self, A, elem):
        # write your code here
        i = j = 0
        while j < len(A):
            if A[j] == elem:
                j += 1
            else:
                A[i] = A[j]
                i += 1
                j += 1

        return i
