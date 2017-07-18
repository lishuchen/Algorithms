#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {string} s  an expression includes numbers, letters and brackets
    # @return {string} a string
    def expressionExpand(self, s):
        # Write your code here
        if not s:
            return ""

        stack = [[1, ""]]
        times = ""
        for ch in s:
            if ch.isdigit():
                times += ch
            elif ch == "[":
                stack.append([int(times), ""])
                times = ""
            elif ch == "]":
                top = stack.pop()
                stack[-1][1] += top[0] * top[1]
            else:
                stack[-1][1] += ch

        return stack[-1][1]
