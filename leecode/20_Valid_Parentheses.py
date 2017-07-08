#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        left = ["(", "{", "["]
        right = {")": 0, "}": 1, "]": 2}
        stack = list()
        for char in s:
            if char in left:
                stack.append(char)
            else:
                index = right[char]
                if not stack or stack[-1] != left[index]:
                    return False
                else:
                    stack.pop()

        return True if not len(stack) else False
