#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, element):
        # write your code here
        self.stack1.append(element)

    def top(self):
        # write your code here
        # return the top element
        if not self.stack2:
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def pop(self):
        # write your code here
        # pop and return the top element
        if not self.stack2:
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
