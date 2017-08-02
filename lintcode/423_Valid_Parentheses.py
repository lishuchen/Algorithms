#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        if not s:
            return True

        stack = list()
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        for ch in s:
            if ch in left:
                stack.append(ch)
            else:
                if not stack or stack[-1] != left[right.index(ch)]:
                    return False
                else:
                    stack.pop()

        return True if not stack else False
