#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k <= 0:
            return []

        hp = list()
        for i in range(min(len(nums2), k)):
            heapq.heappush(hp, (nums2[i] + nums1[0], nums2[i], 0))

        rsl = list()
        for _ in range(k):
            if hp:
                total, val, index = heapq.heappop(hp)
                if index < len(nums1) - 1:
                    heapq.heappush(hp, (val + nums1[index + 1], val, index + 1))

                rsl.append([total - val, val])
            else:
                break

        return rsl
