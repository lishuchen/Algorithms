#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        # write your code here
        if not numbers or target is None:
            return None

        numbers.sort()
        close_sum = sys.maxsize
        for i in range(len(numbers) - 2):
            start = i + 1
            end = len(numbers) - 1
            while start < end:
                total = numbers[i] + numbers[start] + numbers[end]
                if total == target:
                    return total
                else:
                    if abs(total - target) < abs(close_sum - target):
                        close_sum = total
                    if total > target:
                        end -= 1
                    else:
                        start += 1

        return close_sum
