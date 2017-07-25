#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        # Write your code here
        if num == 0:
            return False

        if num in [1, 2, 3, 5]:
            return True

        for factor in [2, 3, 5]:
            n, m = divmod(num, factor)
            if m == 0:
                if self.isUgly(n):
                    return True

        return False
        return False
