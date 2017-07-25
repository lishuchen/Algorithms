#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param {UndirectedGraphNode[]} graph a list of undirected graph node
    # @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    # @param {UndirectedGraphNode} node an Undirected graph node
    # @param {int} target an integer
    # @return {UndirectedGraphNode} a node
    def searchNode(self, graph, values, node, target):
        # Write your code here
        if not graph or not node:
            return None

        dq = collections.deque([node])
        while dq:
            n = dq.popleft()
            if values[n] == target:
                return n
            for nb in n.neighbors:
                if values[nb] == target:
                    return nb
                dq.append(nb)

        return None
