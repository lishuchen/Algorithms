#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import heapq


class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''

    def topk(self, nums, k):
        # Write your code here
        if not nums or k < 1:
            return []

        nums.sort(reverse=True)
        return nums[:k]
