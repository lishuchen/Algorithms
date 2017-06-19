#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sums = list()
        self.lens = len(nums)
        if self.lens > 0:
            self.sums.append(nums[0])
        for index, val in enumerate(nums[1:], 1):
            self.sums.append(val + self.sums[index - 1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.lens == 0 or i > j:
            return 0

        j = min(j, self.lens - 1)
        i = max(i, 0)
        return self.sums[j] if i == 0 else self.sums[j] - self.sums[i - 1]

        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)
