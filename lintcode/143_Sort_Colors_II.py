#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here
        if not colors:
            return None

        self.sortclr(colors, 0, len(colors) - 1, 1, k)

    def sortclr(self, colors, start, end, color_s, color_e):
        if color_s >= color_e or start >= end:
            return

        mid_color = color_s + (color_e - color_s) / 2
        l, r = start, end
        while l <= r:
            while l <= r and colors[l] <= mid_color:
                l += 1
            while l <= r and colors[r] > mid_color:
                r -= 1
            if l <= r:
                colors[l], colors[r] = colors[r], colors[l]
                l += 1
                r -= 1

        self.sortclr(colors, start, l, color_s, mid_color)
        self.sortclr(colors, r, end, mid_color + 1, color_e)
