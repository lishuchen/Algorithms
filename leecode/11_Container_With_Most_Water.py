#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0

        start = 0
        end = len(height) - 1
        max_area = 0
        while start < end:
            base = min(height[start], height[end])
            max_area = max(max_area, (end - start) * base)
            while start < end and height[start] <= base:
                start += 1
            while start < end and height[end] <= base:
                end -= 1

        return max_area
