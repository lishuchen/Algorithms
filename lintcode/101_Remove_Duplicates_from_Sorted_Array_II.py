#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param A: a list of integers
    @return an integer
    """

    def removeDuplicates(self, A):
        # write your code here

        if not A:
            return 0

        size = 0
        count = 0
        for num in A[1:]:
            if num != A[size]:
                count = 0
                size += 1
                A[size] = num
            else:
                if count == 0:
                    size += 1
                    A[size] = num
                    count += 1

        return size + 1
