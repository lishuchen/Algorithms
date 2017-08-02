#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class TwoSum(object):
    def __init__(self):
        # initialize your data structure here
        self.nums = list()

    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        # Write your code here
        self.nums.append(number)

    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        # Write your code here
        dct = dict()
        for num in self.nums:
            if value - num in dct:
                return True
            else:
                dct[num] = 0

        return False



        # Your TwoSum object will be instantiated and called as such:
        # twoSum = TwoSum()
        # twoSum.add(number)
        # twoSum.find(value)
