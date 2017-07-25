#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        if numbers is None or target is None:
            return []

        dct = dict()
        for i, num in enumerate(numbers, 1):
            dif = target - num
            if dif in dct:
                return [dct[dif], i]
            else:
                dct[num] = i

        return []
