#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    def connectedSet2(self, nodes):
        # Write your code here
        if not nodes:
            return []

        dct = dict()
        for node in nodes:
            dct[node.label] = node.label

        for node in nodes:
            label = node.label
            for n in node.neighbors:
                root_node = self.find(dct, label)
                root_n = self.find(dct, n.label)
                dct[root_node] = root_n

        rsl = dict()
        for label in dct.keys():
            root = self.find(dct, label)
            rsl.setdefault(root, []).append(label)

        for lst in rsl.values():
            lst.sort()

        return rsl.values()

    def find(self, dct, label):
        while dct[label] != label:
            label = dct[label]

        return label
