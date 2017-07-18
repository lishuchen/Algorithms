#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import heapq


class Solution:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    def kthSmallestSum(self, A, B, k):
        # Write your code here

        if not A or not B:
            return -1

        hp = list()
        for i in range(min(len(B), k)):
            heapq.heappush(hp, (B[i] + A[0], B[i], 0))

        size_a = len(A)
        for i in range(k):
            sum, val, index = heapq.heappop(hp)
            index += 1
            if index < size_a:
                heapq.heappush(hp, (val + A[index], val, index))

            if i == k - 1:
                return sum

        return -1
