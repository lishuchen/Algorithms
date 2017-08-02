#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        # Write your code here

        cur_max = total_max = A[0]
        start = end = 0
        ans = [0, 0]
        for i, num in enumerate(A[1:], 1):
            if cur_max < 0:
                cur_max = num
                start = i
            else:
                cur_max += num

            if cur_max > total_max:
                ans = [start, i]
                total_max = cur_max

        return ans
