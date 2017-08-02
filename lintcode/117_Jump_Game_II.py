#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return False

        right = 0
        step = 0
        for i, num in enumerate(A):
            if i <= right:
                if i + num > right:
                    right = i + num
                    step += 1
                    if right >= len(A) - 1:
                        return step
            else:
                return 0
