#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        if not start or not end or not dict:
            return 0

        if start == end:
            return 1

        dq = collections.deque([start])
        word_set = set(start)
        step = 0
        while dq:
            step += 1
            size = len(dq)
            for _ in range(size):
                s = dq.popleft()
                for i in range(len(s)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        new_w = s[:i] + ch + s[i + 1:]
                        if new_w == end:
                            return step + 1
                        if new_w not in word_set and new_w in dict:
                            dq.append(new_w)
                            word_set.add(new_w)

        return 0
