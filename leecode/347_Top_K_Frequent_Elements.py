#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        dct = dict()
        for val in nums:
            dct[val] = dct.get(val, 0) + 1

        rsl = [item[0] for item in sorted(dct.items(), key=operator.itemgetter(1), reverse=True)]

        return rsl[:k]


# Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return zip(*collections.Counter(nums).most_common(k))[0]
