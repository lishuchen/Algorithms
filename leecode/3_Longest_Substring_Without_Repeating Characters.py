#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        chars = dict()
        max_len = 0
        start_point = 0
        for i, c in enumerate(s):
            if c in chars:
                start_point = max(chars[c] + 1, start_point)
            max_len = max(max_len, i - start_point + 1)
            chars[c] = i

        return max_len

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("tmmzuxt"))