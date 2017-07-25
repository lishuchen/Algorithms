#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param A : an integer array
    @return : a integer
    """

    def singleNumber(self, A):
        # write your code here
        val = 0
        for num in A:
            val ^= num

        return val
