#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
        if not nodes:
            return nodes

        self.visit = dict()
        for node in nodes:
            self.visit[node.label] = False

        rsl = list()
        for node in nodes:
            node_lst = list()
            self.dfs(node, node_lst)
            if node_lst:
                rsl.append(sorted(node_lst))

        return rsl

    def dfs(self, node, node_list):
        if self.visit[node.label] == False:
            node_list.append(node.label)
            self.visit[node.label] = True

            for nb in node.neighbors:
                self.dfs(nb, node_list)
