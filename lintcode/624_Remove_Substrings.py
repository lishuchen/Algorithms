#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {string} s a string
    # @param {set} dict a set of n substrings
    # @return {int} the minimum length
    def minLength(self, s, dict):
        # Write your code here
        if dict is None or s is None:
            return None

        dq = collections.deque([s])
        hash = set([s])

        min_len = len(s)

        while dq:
            string = dq.popleft()
            for substr in dict:
                start = 0
                while True:
                    idx = string.find(substr, start)
                    if idx != -1:
                        new_s = string[:idx] + string[idx + len(substr):]
                        min_len = min(len(new_s), min_len)
                        start = idx + 1
                        if new_s not in hash:
                            dq.append(new_s)
                            hash.add(new_s)
                    else:
                        break

        return min_len
