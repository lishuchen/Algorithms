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

        count = 0
        for num in A:
            if num != A[count]:
                count += 1
                A[count] = num

        return count + 1
