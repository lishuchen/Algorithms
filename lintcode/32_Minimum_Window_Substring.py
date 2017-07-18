#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """

    def minWindow(self, source, target):
        # write your code here
        if not source or not target or len(source) < len(target):
            return ""

        tar_dct = dict()
        count = len(target)
        for val in target:
            tar_dct[val] = tar_dct.get(val, 0) + 1

        left = right = 0
        len_s = len(source)
        min_size = len_s + 1
        start = -1
        while right < len_s:
            char = source[right]
            if char in tar_dct:
                tar_dct[char] -= 1
                if tar_dct[char] >= 0:
                    count -= 1
            right += 1
            while count == 0:
                lens = right - left
                if lens < min_size:
                    min_size = lens
                    start = left
                c = source[left]
                if c in tar_dct:
                    tar_dct[c] += 1
                    if tar_dct[c] > 0:
                        count += 1
                left += 1

        return "" if start == -1 else source[start: start + min_size]
