#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        nums.sort()
        rsl = []
        for i in range(0, len(nums) - 2):
            # remove duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                val = - nums[i] - nums[k]
                if nums[j] == val:
                    rsl.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j + 1] == nums[j]:
                         j += 1
                    j += 1
                    while j < k and nums[k - 1] == nums[k]:
                         k -= 1
                    k -= 1
                elif nums[j] > val:
                    k -= 1
                else:
                    j += 1

        return rsl

if __name__ == "__main__":
    s = Solution()
    s.threeSum([-1,0,1,2,-1,-4])