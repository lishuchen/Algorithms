#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class ConnectingGraph2:
    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.lst = list(range(n + 1))
        self.size = [1] * len(self.lst)

    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a != root_b:
            self.lst[root_a] = root_b
            self.size[root_b] += self.size[root_a]

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

    # @param {int} a
    # return {int}  the number of nodes connected component
    # which include a node.
    def query(self, a):
        # Write your code here
        root_a = self.find_root(a)
        return self.size[root_a]
