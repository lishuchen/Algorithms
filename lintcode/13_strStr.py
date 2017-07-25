#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None or len(source) < len(target):
            return -1

        if len(target) == 0:
            return 0

        len_t = len(target)
        len_s = len(source)
        for i in range(len_s - len_t + 1):
            k = i
            count = 0
            for c in target:
                if source[k] == c:
                    count += 1
                    k += 1
                else:
                    break

            if count == len_t:
                return i

        return -1
