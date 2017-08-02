#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        if numbers is None or len(numbers) < 3:
            return []

        numbers.sort()
        rsl = list()
        for i in range(len(numbers) - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            start = i + 1
            end = len(numbers) - 1
            while start < end:
                total = numbers[start] + numbers[end]
                if total == -numbers[i]:
                    rsl.append((numbers[i], numbers[start], numbers[end]))
                    start += 1
                    while start < end and numbers[start] == numbers[start - 1]:
                        start += 1
                    end -= 1
                    while start < end and numbers[end] == numbers[end + 1]:
                        end -= 1
                elif total > -numbers[i]:
                    end -= 1
                else:
                    start += 1

        return rsl
