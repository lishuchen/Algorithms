#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class ConnectingGraph:
    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.lst = [i for i in range(n + 1)]

    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        root_a = self.find_root(a)
        root_b = self.find_root(b)
        self.lst[root_b] = root_a

    def find_root(self, a):
        cur = a
        while self.lst[cur] != cur:
            cur = self.lst[cur]

        root = cur
        while self.lst[a] != root:
            parent = self.lst[a]
            self.lst[a] = root
            a = parent

        return root

    # @param {int} a, b
    # return {boolean} true if they are connected or false
    def query(self, a, b):
        # Write your code here
        return self.find_root(a) == self.find_root(b)
