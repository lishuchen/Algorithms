#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order
    def findOrder(self, numCourses, prerequisites):
        # Write your code here
        if numCourses <= 0:
            return []

        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for relation in prerequisites:
            crs, pre = relation
            graph[pre].append(crs)
            indegrees[crs] += 1

        zero_indgr = collections.deque()
        for index, val in enumerate(indegrees):
            if val == 0:
                zero_indgr.append(index)

        order = list()
        while zero_indgr:
            node = zero_indgr.popleft()
            order.append(node)
            for num in graph[node]:
                indegrees[num] -= 1
                if indegrees[num] == 0:
                    zero_indgr.append(num)

        return order if len(order) == numCourses else []
