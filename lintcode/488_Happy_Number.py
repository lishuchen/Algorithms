#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        if n < 1:
            return False

        dct = dict()
        while True:
            new_num = 0
            while n:
                n, d = divmod(n, 10)
                new_num += d ** 2

            if new_num == 1:
                return True
            else:
                if new_num in dct:
                    return False
                else:
                    dct[new_num] = 1
                    n = new_num
