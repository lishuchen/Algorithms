#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        profit = [0, nums[0]]
        for i in range(2, len(nums) + 1):
            profit[i%2] = max(nums[i-1] + profit[(i-2)%2], profit[(i-1)%2])

        return profit[len(nums) % 2]

if __name__ == '__main__':
    s = Solution()
    print(s.rob([1,2,3,4,5]))