#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {string} source a source string
    # @param {string} target a target string
    # @return {int} an integer as index
    def strStr2(self, source, target):
        # Write your code here
        if source is None or target is None:
            return -1

        if target == "" or source == target:
            return 0

        size_s = len(source)
        size_t = len(target)

        mod = sys.maxsize - 1234567890
        hash_target = 0
        power = 1
        for i in xrange(size_t):
            hash_target = (hash_target * 31 + ord(target[i]) - ord('a')) % mod
            if hash_target < 0:
                hash_target += mod
            power = (power * 31) % mod

        code = 0
        for i in xrange(size_s):
            code = (code * 31 + ord(source[i]) - ord('a')) % mod
            if i >= len(target):
                code = (code - power * (ord(source[i - size_t]) - ord('a'))) % mod
                if code < 0:
                    code += mod

            if code == hash_target and source[i - size_t + 1: i + 1] == target:
                return i - size_t + 1

        return -1
