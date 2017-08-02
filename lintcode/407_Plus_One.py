#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        if not digits:
            return []

        flag, digits[-1] = divmod(digits[-1] + 1, 10)
        for i in range(len(digits) - 2, -1, -1):
            flag, digits[i] = divmod(digits[i] + flag, 10)

        return digits if flag == 0 else [1] + digits
