#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class MinStack(object):
    def __init__(self):
        # do some intialize if necessary
        self.stack = list()
        self.mins = list()

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if not self.mins or number <= self.mins[-1]:
            self.mins.append(number)

    def pop(self):
        # pop and return the top item in stack
        top = self.stack.pop()
        if self.mins[-1] == top:
            self.mins.pop()

        return top

    def min(self):
        # return the minimum number in stack
        return self.mins[-1]
