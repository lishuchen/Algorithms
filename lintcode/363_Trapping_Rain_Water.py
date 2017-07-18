#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0

        start, end = 0, len(heights) - 1
        vol = 0
        while start < end:
            min_ht = min(heights[start], heights[end])
            while start < end and heights[start] <= min_ht:
                vol += min_ht - heights[start]
                start += 1
            while start < end and heights[end] <= min_ht:
                vol += min_ht - heights[end]
                end -= 1

        return vol
