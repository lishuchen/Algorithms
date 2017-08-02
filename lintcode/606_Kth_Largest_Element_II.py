#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import heapq


class Solution:
    # @param nums {int[]} an integer unsorted array
    # @param k {int} an integer from 1 to n
    # @return {int} the kth largest element
    def kthLargestElement2(self, nums, k):
        # Write your code here
        if not nums or k < 1:
            return

        hp = []
        for n in nums:
            if len(hp) >= k:
                heapq.heappushpop(hp, n)
            else:
                heapq.heappush(hp, n)

        return hp[0]
