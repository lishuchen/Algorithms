#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""


class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        # write your code here
        start = 0
        end = 1
        while reader.get(end) < target and reader.get(end) != sys.maxsize:
            start = end
            end *= 2

        while start < end:
            mid = start + ((end - start) >> 1)
            if reader.get(mid) == sys.maxsize:
                end = mid - 1
            else:
                if reader.get(mid) >= target:
                    end = mid
                else:
                    start = mid + 1

        return start if target == reader.get(start) else -1
