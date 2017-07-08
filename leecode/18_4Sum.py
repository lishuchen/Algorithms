#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 4:
            return []

        nums.sort()
        rsl = list()
        for i in range(len(nums) - 3):
            if target < nums[i] * 4 or target > nums[-1] * 4:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                val = target - nums[i] - nums[j]
                start = j + 1
                end = len(nums) - 1
                while start < end:
                    add = nums[start] + nums[end]
                    if add == val:
                        rsl.append([nums[i], nums[j], nums[start], nums[end]])
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1
                        end -= 1
                    elif add > val:
                        end -= 1
                    else:
                        start += 1

        return rsl
