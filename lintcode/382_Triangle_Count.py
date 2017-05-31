#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # write your code here
        arr = sorted(S)
        count = 0
        for i in range(2, len(arr)):
            count += self.count(arr, i)

        return count

    def count(self, arr, i):
        h = 0
        t = i - 1
        count = 0
        while h < t:
            sum = arr[h] + arr[t]
            if sum > arr[i]:
                count += t - h
                t -= 1
            elif sum <= arr[i]:
                h += 1

        return count
