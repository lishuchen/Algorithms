#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        size = len(height)
        start = end = 0
        for i in range(size):
            if height[i] > 0:
                start = i
                break
        for i in range(size - 1, -1, -1):
            if height[i] > 0:
                end = i
                break

        count = 0
        left = height[start]
        right = height[end]
        while start < end:
            if left < right:
                start += 1
                if height[start] <= left:
                    count += left - height[start]
                else:
                    left = height[start]
            else:
                end -= 1
                if height[end] <= right:
                    count += right - height[end]
                else:
                    right = height[end]

        return count