#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Solution 1: two pointers
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if not s1 or not s2 or len(s1) > len(s2):
            return False

        count = len(s1)
        tar = dict()
        for c in s1:
            tar[c] = tar.get(c, 0) + 1

        org_tar = dict(tar)
        begin = 0
        end = 0
        while end < len(s2):
            ch = s2[end]
            if ch not in tar:
                org_tar = dict(tar)
                count = len(s1)
                begin = end + 1
            else:
                org_tar[ch] -= 1
                if org_tar[ch] >= 0:
                    count -= 1
                    if count == 0:
                        return True
                else:
                    while org_tar[ch] < 0 and begin < end:
                        org_tar[s2[begin]] += 1
                        if org_tar[s2[begin]] > 0:
                            count += 1
                        begin += 1

            end += 1

        return False


# Solution 2: sliding  windows
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if not s1 or not s2 or len(s1) > len(s2):
            return False

        count = [0] * 26
        for i in range(len(s2)):
            if i < len(s1):
                count[ord(s1[i]) - ord('a')] += 1
                count[ord(s2[i]) - ord('a')] -= 1
            else:
                count[ord(s2[i]) - ord('a')] -= 1
                count[ord(s2[i - len(s1)]) - ord('a')] += 1

            if i >= len(s1) - 1:
                if len(filter(lambda x: x != 0, count)) == 0:
                    return True

        return False
