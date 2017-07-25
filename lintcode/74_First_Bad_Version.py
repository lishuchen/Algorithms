#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """

    def findFirstBadVersion(self, n):
        # write your code here
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) / 2
            if not SVNRepo.isBadVersion(mid):
                start = mid
            else:
                end = mid

        if SVNRepo.isBadVersion(start):
            return start
        return end
