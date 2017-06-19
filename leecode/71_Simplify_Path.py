#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = list()
        for name in path.split("/"):
            if name == '.':
                continue
            elif name == '..':
                if stack:
                    stack.pop()
            elif name != "":
                stack.append(name)

        return "/" + "/".join(stack)
